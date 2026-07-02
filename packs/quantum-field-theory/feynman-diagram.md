---
title: "Feynman diagram"
source: https://en.wikipedia.org/wiki/Feynman_diagram
domain: quantum-field-theory
license: CC-BY-SA-4.0
tags: quantum field theory, gauge theory, feynman diagram, path integral formulation
fetched: 2026-07-02
---

# Feynman diagram

In theoretical physics, a **Feynman diagram** is a pictorial representation of the mathematical expressions describing the behavior and interaction of subatomic particles. The scheme is named after American physicist Richard Feynman, who introduced the diagrams in 1948.

The calculation of probability amplitudes in theoretical particle physics requires the use of large, complicated integrals over a large number of variables. Feynman diagrams instead represent these integrals graphically.

Feynman diagrams give a simple visualization of what would otherwise be an arcane and abstract formula. According to David Kaiser, "Since the middle of the 20th century, theoretical physicists have increasingly turned to this tool to help them undertake critical calculations. Feynman diagrams have revolutionized nearly every aspect of theoretical physics."

While the diagrams apply primarily to quantum field theory, they can be used in other areas of physics, such as solid-state theory. Frank Wilczek wrote that the calculations that won him the 2004 Nobel Prize in Physics "would have been literally unthinkable without Feynman diagrams, as would [Wilczek's] calculations that established a route to production and observation of the Higgs particle."

A Feynman diagram is a graphical representation of a perturbative contribution to the transition amplitude or correlation function of a quantum mechanical or statistical field theory. Within the canonical formulation of quantum field theory, a Feynman diagram represents a term in the Wick's expansion of the perturbative S-matrix. Alternatively, the path integral formulation of quantum field theory represents the transition amplitude as a weighted sum of all possible histories of the system from the initial to the final state, in terms of either particles or fields. The transition amplitude is then given as the matrix element of the S-matrix between the initial and final states of the quantum system.

Feynman used Ernst Stueckelberg's interpretation of the positron as if it were an electron moving backward in time. Thus, antiparticles are represented as moving backward along the time axis in Feynman diagrams.

## Motivation and history

When calculating scattering cross-sections in particle physics, the interaction between particles can be described by starting from a free field that describes the incoming and outgoing particles, and including an interaction Hamiltonian to describe how the particles deflect one another. The amplitude for scattering is the sum of each possible interaction history over all possible intermediate particle states. The number of times the interaction Hamiltonian acts is the order of the perturbation expansion, and the time-dependent perturbation theory for fields is known as the Dyson series. When the intermediate states at intermediate times are energy eigenstates (collections of particles with a definite momentum) the series is called old-fashioned perturbation theory (or time-dependent/time-ordered perturbation theory).

The Dyson series can be alternatively rewritten as a sum over Feynman diagrams, where at each vertex both the energy and momentum are conserved, but where the length of the energy-momentum four-vector is not necessarily equal to the mass, i.e. the intermediate particles are so-called off-shell. The Feynman diagrams are much easier to keep track of than "old-fashioned" terms, because the old-fashioned way treats the particle and antiparticle contributions as separate. Each Feynman diagram is the sum of exponentially many old-fashioned terms, because each internal line can separately represent either a particle or an antiparticle. In a non-relativistic classical theory, there are no antiparticles and there is no doubling, so each Feynman diagram includes only one term.

Feynman gave a prescription for calculating the amplitude (the Feynman rules, below) for any given diagram from a field theory Lagrangian. Each internal line corresponds to a factor of the virtual particle's propagator; each vertex where lines meet gives a factor derived from an interaction term in the Lagrangian, and incoming and outgoing lines carry an energy, momentum, and spin.

In addition to their value as a mathematical tool, Feynman diagrams provide deep physical insight into the nature of particle interactions. Particles interact in every way available; in fact, intermediate virtual particles are allowed to propagate faster than light. The probability of each final state is then obtained by summing over all such possibilities. This is closely tied to the functional integral formulation of quantum mechanics, also invented by Feynman—see path integral formulation.

The naïve application of such calculations often produces diagrams whose amplitudes are infinite, because the short-distance particle interactions require a careful limiting procedure, to include particle self-interactions. The technique of renormalization, suggested by Ernst Stueckelberg and Hans Bethe and implemented by Dyson, Feynman, Schwinger, and Tomonaga compensates for this effect and eliminates the troublesome infinities. After renormalization, calculations using Feynman diagrams match experimental results with very high accuracy.

Feynman diagram and path integral methods are also used in statistical mechanics and can even be applied to classical mechanics.

### Alternate names

Murray Gell-Mann always referred to Feynman diagrams as **Stueckelberg diagrams**, after Swiss physicist Ernst Stueckelberg, who devised a similar notation many years earlier. Stueckelberg was motivated by the need for a manifestly covariant formalism for quantum field theory, but did not provide as automated a way to handle symmetry factors and loops, although he was first to find the correct physical interpretation in terms of forward and backward in time particle paths, all without the path-integral.

Historically, as a book-keeping device of covariant perturbation theory, the graphs were called **Feynman–Dyson diagrams** or **Dyson graphs**, because the path integral was unfamiliar when they were introduced, and Freeman Dyson's derivation from old-fashioned perturbation theory borrowed from the perturbative expansions in statistical mechanics was easier to follow for physicists trained in earlier methods. Feynman had to lobby hard for the diagrams, which confused physicists trained in equations and graphs.

## Representation of physical reality

In their presentations of fundamental interactions, written from the particle physics perspective, Gerard 't Hooft and Martinus Veltman gave good arguments for taking the original, non-regularized Feynman diagrams as the most succinct representation of the physics of quantum scattering of fundamental particles. Their motivations are consistent with the convictions of James Daniel Bjorken and Sidney Drell:

> The Feynman graphs and rules of calculation summarize quantum field theory in a form in close contact with the experimental numbers one wants to understand. Although the statement of the theory in terms of graphs may imply perturbation theory, use of graphical methods in the many-body problem shows that this formalism is flexible enough to deal with phenomena of nonperturbative characters ... Some modification of the Feynman rules of calculation may well outlive the elaborate mathematical structure of local canonical quantum field theory ...

In quantum field theories, Feynman diagrams are obtained from a Lagrangian by Feynman rules.

Dimensional regularization is a method for regularizing integrals in the evaluation of Feynman diagrams; it assigns values to them that are meromorphic functions of an auxiliary complex parameter d, called the dimension. Dimensional regularization writes a Feynman integral as an integral depending on the spacetime dimension d and spacetime points.

## Particle-path interpretation

A Feynman diagram is a representation of quantum field theory processes in terms of particle interactions. The particles are represented by the diagram lines. The lines can be squiggly or straight, with an arrow or without, depending on the type of particle. A point where lines connect to other lines is a vertex, and this is where the particles meet and interact. The interactions are: emit/absorb particles, deflect particles, or change particle type.

The three different types of lines are: internal lines, connecting vertices; incoming lines, extending from "the past" to a vertex, representing an initial state; and outgoing lines, extending from a vertex to "the future", representing the end state (the latter two are also known as external lines). Traditionally, the bottom of the diagram is the past and the top the future; alternatively, the past is to the left and the future to the right. When calculating correlation functions instead of scattering amplitudes, past and future are not relevant and all lines are internal. The particles then begin and end on small x's, which represent the positions of the operators whose correlation is calculated.

Feynman diagrams are a pictorial representation of a contribution to the total amplitude for a process that can happen in different ways. When a group of incoming particles scatter off each other, the process can be thought of as one where the particles travel over all possible paths, including paths that go backward in time.

Feynman diagrams are graphs that represent the interaction of particles rather than the physical position of the particle during a scattering process. They are not the same as spacetime diagrams and bubble chamber images even though they all describe particle scattering. Unlike a bubble chamber picture, only the sum of all relevant Feynman diagrams represent any given particle interaction; particles do not choose a particular diagram each time they interact. The law of summation is in accord with the principle of superposition—every diagram contributes to the total process's amplitude.

## Description

A Feynman diagram represents a perturbative contribution to the amplitude of a quantum transition from some initial quantum state to some final quantum state.

For example, in the process of electron-positron annihilation the initial state is one electron and one positron, while the final state is two photons.

Conventionally, the initial state is at the left of the diagram and the final state at the right (although other layouts are also used).

The particles in the initial state are depicted by lines pointing in the direction of the initial state (e.g., to the left). The particles in the final state are represented by lines pointing in the direction of the final state (e.g., to the right).

QED involves two types of particles: matter particles such as electrons or positrons (called fermions) and exchange particles (called gauge bosons). They are represented in Feynman diagrams as follows:

- Electron in the initial state is represented by a solid line, with an arrow indicating the spin of the particle e.g. pointing toward the vertex (→•).
- Electron in the final state is represented by a line, with an arrow indicating the spin of the particle e.g. pointing away from the vertex: (•→).
- Positron in the initial state is represented by a solid line, with an arrow indicating the spin of the particle e.g. pointing away from the vertex: (←•).
- Positron in the final state is represented by a line, with an arrow indicating the spin of the particle e.g. pointing toward the vertex: (•←).
- Virtual Photon in the initial and the final states is represented by a wavy line (~• and •~).

In QED each vertex has three lines attached to it: one bosonic line, one fermionic line with arrow toward the vertex, and one fermionic line with arrow away from the vertex.

Vertices can be connected by a bosonic or fermionic propagator. A bosonic propagator is represented by a wavy line connecting two vertices (•~•). A fermionic propagator is represented by a solid line with an arrow connecting two vertices, (•←•).

The number of vertices gives the order of the term in the perturbation series expansion of the transition amplitude.

### Electron–positron annihilation example

The electron–positron annihilation interaction:

e

+

+ e

−

→ 2γ

has a contribution from the second order Feynman diagram:

In the initial state (at the bottom; early time) there is one electron (e−) and one positron (e+) and in the final state (at the top; late time) there are two photons (γ).

## Canonical quantization formulation

The probability amplitude for a transition of a quantum system (between asymptotically free states) from the initial state |i⟩ to the final state | f ⟩ is given by the matrix element

$S_{\rm {fi}}=\langle \mathrm {f} |S|\mathrm {i} \rangle \;,$

where S is the S-matrix. In terms of the time-evolution operator U, it is simply

$S=\lim _{t_{2}\rightarrow +\infty }\left[\lim _{t_{1}\rightarrow -\infty }U(t_{2},t_{1})\right]\;.$

In the interaction picture, this expands to

$S={\mathcal {T}}\exp \left(-i\int _{-\infty }^{+\infty }d\tau H_{V}(\tau )\right).$

where HV is the interaction Hamiltonian and ${\mathcal {T}}$ signifies the time-ordered product of operators. Dyson's formula expands the time-ordered matrix exponential into a perturbation series in the powers of the interaction Hamiltonian density,

$S=\sum _{n=0}^{\infty }{\frac {(-i)^{n}}{n!}}\left(\prod _{j=1}^{n}\int d^{4}x_{j}\right){\mathcal {T}}\left\{\prod _{j=1}^{n}{\mathcal {H}}_{V}\left(x_{j}\right)\right\}\equiv \sum _{n=0}^{\infty }S^{(n)}\;.$

Equivalently, with the interaction Lagrangian LV, it is

$S=\sum _{n=0}^{\infty }{\frac {i^{n}}{n!}}\left(\prod _{j=1}^{n}\int d^{4}x_{j}\right){\mathcal {T}}\left\{\prod _{j=1}^{n}{\mathcal {L}}_{V}\left(x_{j}\right)\right\}\equiv \sum _{n=0}^{\infty }S^{(n)}\;.$

A Feynman diagram is a graphical representation of a single summand in the Wick's expansion of the time-ordered product in the nth-order term *S*(*n*) of the Dyson series of the S-matrix,

${\mathcal {T}}\prod _{j=1}^{n}{\mathcal {L}}_{V}\left(x_{j}\right)=\sum _{\text{A}}(\pm ){\mathcal {N}}\prod _{j=1}^{n}{\mathcal {L}}_{V}\left(x_{j}\right)\;,$

where *N* signifies the normal-ordered product of the operators and (±) takes care of the possible sign change when commuting the fermionic operators to bring them together for a contraction (a propagator) and *A* represents all possible contractions.

### Feynman rules

The diagrams are drawn according to the Feynman rules, which depend upon the interaction Lagrangian. For the QED interaction Lagrangian

$L_{v}=-g{\bar {\psi }}\gamma ^{\mu }\psi A_{\mu }$

describing the interaction of a fermionic field ψ with a bosonic gauge field Aμ, the Feynman rules can be formulated in coordinate space as follows:

- Each integration coordinate xj is represented by a point (sometimes called a vertex);
- A bosonic propagator is represented by a wiggly line connecting two points;
- A fermionic propagator is represented by a solid line connecting two points;
- A bosonic field $A_{\mu }(x_{i})$ is represented by a wiggly line attached to the point xi;
- A fermionic field *ψ*(*xi*) is represented by a solid line attached to the point xi with an arrow toward the point;
- An anti-fermionic field *ψ*(*xi*) is represented by a solid line attached to the point xi with an arrow away from the point;

### Example: second order processes in QED

The second order perturbation term in the S-matrix is

$S^{(2)}={\frac {(ie)^{2}}{2!}}\int d^{4}x\,d^{4}x'\,T{\bar {\psi }}(x)\,\gamma ^{\mu }\,\psi (x)\,A_{\mu }(x)\,{\bar {\psi }}(x')\,\gamma ^{\nu }\,\psi (x')\,A_{\nu }(x').\;$

#### Scattering of fermions

|   |
|---|

The Wick's expansion of the integrand gives (among others) the following term

$N{\bar {\psi }}(x)\gamma ^{\mu }\psi (x){\bar {\psi }}(x')\gamma ^{\nu }\psi (x'){\underline {A_{\mu }(x)A_{\nu }(x')}}\;,$

where

${\underline {A_{\mu }(x)A_{\nu }(x')}}=\int {\frac {d^{4}k}{(2\pi )^{4}}}{\frac {-ig_{\mu \nu }}{k^{2}+i0}}e^{-ik(x-x')}$

is the electromagnetic contraction (propagator) in the Feynman gauge. This term is represented by the Feynman diagram at the right. This diagram gives contributions to the following processes:

1. e− e− scattering (initial state at the right, final state at the left of the diagram);
2. e+ e+ scattering (initial state at the left, final state at the right of the diagram);
3. e− e+ scattering (initial state at the bottom/top, final state at the top/bottom of the diagram).

#### Compton scattering and annihilation/generation of e− e+ pairs

Another interesting term in the expansion is

$N{\bar {\psi }}(x)\,\gamma ^{\mu }\,{\underline {\psi (x)\,{\bar {\psi }}(x')}}\,\gamma ^{\nu }\,\psi (x')\,A_{\mu }(x)\,A_{\nu }(x')\;,$

where

${\underline {\psi (x){\bar {\psi }}(x')}}=\int {\frac {d^{4}p}{(2\pi )^{4}}}{\frac {i}{\gamma p-m+i0}}e^{-ip(x-x')}$

is the fermionic contraction (propagator).

## Path integral formulation

In a path integral, the field Lagrangian, integrated over all possible field histories, defines the probability amplitude to go from one field configuration to another. In order to make sense, the field theory must have a well-defined ground state, and the integral must be performed a little bit rotated into imaginary time, i.e. a Wick rotation. The path integral formalism is completely equivalent to the canonical operator formalism above.

### Scalar field Lagrangian

An example is the free relativistic scalar field in d dimensions, whose action integral is:

$S=\int {\tfrac {1}{2}}\partial _{\mu }\phi \partial ^{\mu }\phi \,d^{d}x\,.$

The unnormalized probability amplitude for a process is:

$\int _{A}^{B}e^{iS}\,D\phi \,,$

where A and B are space-like hypersurfaces that define the boundary conditions. The collection of all the *φ*(*A*) on the starting hypersurface give the field's initial value, analogous to the starting position for a point particle, and the field values *φ*(*B*) at each point of the final hypersurface defines the final field value, which is allowed to vary, giving a different amplitude to end up at different values. This is the field-to-field transition amplitude.

The path integral gives the expectation value of operators between the initial and final state:

$\int _{A}^{B}e^{iS}\phi (x_{1})\cdots \phi (x_{n})\,D\phi =\left\langle A\left|\phi (x_{1})\cdots \phi (x_{n})\right|B\right\rangle \,,$

and in the limit that A and B recede to the infinite past and the infinite future, the only contribution that matters is from the ground state (this is only rigorously true if the path-integral is defined slightly rotated into imaginary time). The path integral is normalized in the following way:

${\frac {\displaystyle \int e^{iS}\phi (x_{1})\cdots \phi (x_{n})\,D\phi }{\displaystyle \int e^{iS}\,D\phi }}=\left\langle 0\left|\phi (x_{1})\cdots \phi (x_{n})\right|0\right\rangle \,.$

The field's partition function is the normalization factor on the bottom, which coincides with the statistical mechanical partition function at zero temperature when rotated into imaginary time.

The initial-to-final amplitudes are ill-defined if one thinks of the continuum limit right from the beginning, because the fluctuations in the field can become unbounded. So the path-integral can be thought of as on a discrete square lattice, with lattice spacing a and the limit *a* → 0 should be taken carefully. If the final results do not depend on the shape of the lattice or the value of a, then the continuum limit exists.

### On a lattice

On a lattice, (i), the field can be expanded in Fourier modes:

$\phi (x)=\int {\frac {dk}{(2\pi )^{d}}}\phi (k)e^{ik\cdot x}=\int _{k}\phi (k)e^{ikx}\,.$

Here the integration domain is over k restricted to a cube of side length ⁠2π/*a*⁠, so that large values of k are not allowed. The k-measure contains the factors of 2π from Fourier transforms, this is the best standard convention for k-integrals in QFT. The lattice means that fluctuations at large k are not allowed to contribute right away, they only start to contribute in the limit *a* → 0. Sometimes, instead of a lattice, the field modes are just cut off at high values of k instead.

It is also convenient from time to time to consider the space-time volume to be finite, so that the k modes are also a lattice. This is not strictly as necessary as the space-lattice limit, because interactions in k are not localized, but it is convenient for keeping track of the factors in front of the k-integrals and the momentum-conserving delta functions that will arise.

On a lattice, (ii), the action needs to be discretized:

$S=\sum _{\langle x,y\rangle }{\tfrac {1}{2}}{\big (}\phi (x)-\phi (y){\big )}^{2}\,,$

where ⟨*x*,*y*⟩ is a pair of nearest lattice neighbors x and y. The discretization should be thought of as defining what the derivative ∂*μ**φ* means.

In terms of the lattice Fourier modes, the action can be written:

$S=\int _{k}{\Big (}{\big (}1-\cos(k_{1}){\big )}+{\big (}1-\cos(k_{2}){\big )}+\cdots +{\big (}1-\cos(k_{d}){\big )}{\Big )}\phi _{k}^{*}\phi ^{k}\,.$

For k near zero this is:

$S=\int _{k}{\tfrac {1}{2}}k^{2}\left|\phi (k)\right|^{2}\,.$

Now we have the continuum Fourier transform of the original action. In finite volume, the quantity ddk is not infinitesimal, but becomes the volume of a box made by neighboring Fourier modes, or (⁠2π/*V*⁠)*d*  .

The field φ is real-valued, so the Fourier transform obeys:

$\phi (k)^{*}=\phi (-k)\,.$

In terms of real and imaginary parts, the real part of *φ*(*k*) is an even function of k, while the imaginary part is odd. The Fourier transform avoids double-counting, so that it can be written:

$S=\int _{k}{\tfrac {1}{2}}k^{2}\phi (k)\phi (-k)$

over an integration domain that integrates over each pair (*k*,−*k*) exactly once.

For a complex scalar field with action

$S=\int {\tfrac {1}{2}}\partial _{\mu }\phi ^{*}\partial ^{\mu }\phi \,d^{d}x$

the Fourier transform is unconstrained:

$S=\int _{k}{\tfrac {1}{2}}k^{2}\left|\phi (k)\right|^{2}$

and the integral is over all k.

Integrating over all different values of *φ*(*x*) is equivalent to integrating over all Fourier modes, because taking a Fourier transform is a unitary linear transformation of field coordinates. When you change coordinates in a multidimensional integral by a linear transformation, the value of the new integral is given by the determinant of the transformation matrix. If

$y_{i}=A_{ij}x_{j}\,,$

then

$\det(A)\int dx_{1}\,dx_{2}\cdots \,dx_{n}=\int dy_{1}\,dy_{2}\cdots \,dy_{n}\,.$

If A is a rotation, then

$A^{\mathrm {T} }A=I$

so that det *A* = ±1, and the sign depends on whether the rotation includes a reflection or not.

The matrix that changes coordinates from *φ*(*x*) to *φ*(*k*) can be read off from the definition of a Fourier transform.

$A_{kx}=e^{ikx}\,$

and the Fourier inversion theorem tells you the inverse:

$A_{kx}^{-1}=e^{-ikx}\,$

which is the complex conjugate-transpose, up to factors of 2π. On a finite volume lattice, the determinant is nonzero and independent of the field values.

$\det A=1\,$

and the path integral is a separate factor at each value of k.

$\int \exp \left({\frac {i}{2}}\sum _{k}k^{2}\phi ^{*}(k)\phi (k)\right)\,D\phi =\prod _{k}\int _{\phi _{k}}e^{{\frac {i}{2}}k^{2}\left|\phi _{k}\right|^{2}\,d^{d}k}\,$

The factor ddk is the infinitesimal volume of a discrete cell in k-space, in a square lattice box

$d^{d}k=\left({\frac {1}{L}}\right)^{d}\,,$

where L is the side-length of the box. Each separate factor is an oscillatory Gaussian, and the width of the Gaussian diverges as the volume goes to infinity.

In imaginary time, the *Euclidean action* becomes positive definite, and can be interpreted as a probability distribution. The probability of a field having values φk is

$e^{\int _{k}-{\tfrac {1}{2}}k^{2}\phi _{k}^{*}\phi _{k}}=\prod _{k}e^{-k^{2}\left|\phi _{k}\right|^{2}\,d^{d}k}\,.$

The expectation value of the field is the statistical expectation value of the field when chosen according to the probability distribution:

$\left\langle \phi (x_{1})\cdots \phi (x_{n})\right\rangle ={\frac {\displaystyle \int e^{-S}\phi (x_{1})\cdots \phi (x_{n})\,D\phi }{\displaystyle \int e^{-S}\,D\phi }}$

Since the probability of φk is a product, the value of φk at each separate value of k is independently Gaussian distributed. The variance of the Gaussian is ⁠1/*k*2*ddk*⁠, which is formally infinite, but that just means that the fluctuations are unbounded in infinite volume. In any finite volume, the integral is replaced by a discrete sum, and the variance of the integral is ⁠*V*/*k*2⁠.

### Monte Carlo

The path integral defines a probabilistic algorithm to generate a Euclidean scalar field configuration. Randomly pick the real and imaginary parts of each Fourier mode at wavenumber k to be a Gaussian random variable with variance ⁠1/*k*2⁠. This generates a configuration *φC*(*k*) at random, and the Fourier transform gives *φC*(*x*). For real scalar fields, the algorithm must generate only one of each pair *φ*(*k*), *φ*(−*k*), and make the second the complex conjugate of the first.

To find any correlation function, generate a field again and again by this procedure, and find the statistical average:

$\left\langle \phi (x_{1})\cdots \phi (x_{n})\right\rangle =\lim _{|C|\rightarrow \infty }{\frac {\displaystyle \sum _{C}\phi _{C}(x_{1})\cdots \phi _{C}(x_{n})}{|C|}}$

where |*C*| is the number of configurations, and the sum is of the product of the field values on each configuration. The Euclidean correlation function is just the same as the correlation function in statistics or statistical mechanics. The quantum mechanical correlation functions are an analytic continuation of the Euclidean correlation functions.

For free fields with a quadratic action, the probability distribution is a high-dimensional Gaussian, and the statistical average is given by an explicit formula. But the Monte Carlo method also works well for bosonic interacting field theories where there is no closed form for the correlation functions.

### Scalar propagator

Each mode is independently Gaussian distributed. The expectation of field modes is easy to calculate:

$\left\langle \phi _{k}\phi _{k'}\right\rangle =0\,$

for *k* ≠ *k*′, since then the two Gaussian random variables are independent and both have zero mean.

$\left\langle \phi _{k}\phi _{k}\right\rangle ={\frac {V}{k^{2}}}$

in finite volume V, when the two k-values coincide, since this is the variance of the Gaussian. In the infinite volume limit,

$\left\langle \phi (k)\phi (k')\right\rangle =\delta (k-k'){\frac {1}{k^{2}}}$

Strictly speaking, this is an approximation: the lattice propagator is:

$\left\langle \phi (k)\phi (k')\right\rangle =\delta (k-k'){\frac {1}{2{\big (}d-\cos(k_{1})+\cos(k_{2})\cdots +\cos(k_{d}){\big )}}}$

But near *k* = 0, for field fluctuations long compared to the lattice spacing, the two forms coincide.

The delta functions contain factors of 2π, so that they cancel out the 2π factors in the measure for k integrals.

$\delta (k)=(2\pi )^{d}\delta _{D}(k_{1})\delta _{D}(k_{2})\cdots \delta _{D}(k_{d})\,$

where *δD*(*k*) is the ordinary one-dimensional Dirac delta function. This convention for delta-functions is not universal—some authors keep the factors of 2π in the delta functions (and in the k-integration) explicit.

### Equation of motion

The form of the propagator can be more easily found by using the equation of motion for the field. From the Lagrangian, the equation of motion is:

$\partial _{\mu }\partial ^{\mu }\phi =0\,$

and in an expectation value, this says:

$\partial _{\mu }\partial ^{\mu }\left\langle \phi (x)\phi (y)\right\rangle =0$

Where the derivatives act on x, and the identity is true everywhere except when x and y coincide, and the operator order matters. The form of the singularity can be understood from the canonical commutation relations to be a delta-function. Defining the (Euclidean) *Feynman propagator* Δ as the Fourier transform of the time-ordered two-point function (the one that comes from the path-integral):

$\partial ^{2}\Delta (x)=i\delta (x)\,$

So that:

$\Delta (k)={\frac {i}{k^{2}}}$

If the equations of motion are linear, the propagator will always be the reciprocal of the quadratic-form matrix that defines the free Lagrangian, since this gives the equations of motion. This is also easy to see directly from the path integral. The factor of i disappears in the Euclidean theory.

#### Wick theorem

Because each field mode is an independent Gaussian, the expectation values for the product of many field modes obeys *Wick's theorem*:

$\left\langle \phi (k_{1})\phi (k_{2})\cdots \phi (k_{n})\right\rangle$

is zero unless the field modes coincide in pairs. This means that it is zero for an odd number of φ, and for an even number of φ, it is equal to a contribution from each pair separately, with a delta function.

$\left\langle \phi (k_{1})\cdots \phi (k_{2n})\right\rangle =\sum \prod _{i,j}{\frac {\delta \left(k_{i}-k_{j}\right)}{k_{i}^{2}}}$

where the sum is over each partition of the field modes into pairs, and the product is over the pairs. For example,

$\left\langle \phi (k_{1})\phi (k_{2})\phi (k_{3})\phi (k_{4})\right\rangle ={\frac {\delta (k_{1}-k_{2})}{k_{1}^{2}}}{\frac {\delta (k_{3}-k_{4})}{k_{3}^{2}}}+{\frac {\delta (k_{1}-k_{3})}{k_{3}^{2}}}{\frac {\delta (k_{2}-k_{4})}{k_{2}^{2}}}+{\frac {\delta (k_{1}-k_{4})}{k_{1}^{2}}}{\frac {\delta (k_{2}-k_{3})}{k_{2}^{2}}}$

An interpretation of Wick's theorem is that each field insertion can be thought of as a dangling line, and the expectation value is calculated by linking up the lines in pairs, putting a delta function factor that ensures that the momentum of each partner in the pair is equal, and dividing by the propagator.

#### Higher Gaussian moments — completing Wick's theorem

There is a subtle point left before Wick's theorem is proved—what if more than two of the $\phi$ s have the same momentum? If it's an odd number, the integral is zero; negative values cancel with the positive values. But if the number is even, the integral is positive. The previous demonstration assumed that the $\phi$ s would only match up in pairs.

But the theorem is correct even when arbitrarily many of the $\phi$ are equal, and this is a notable property of Gaussian integration:

$I=\int e^{-ax^{2}/2}dx={\sqrt {\frac {2\pi }{a}}}$

${\frac {\partial ^{n}}{\partial a^{n}}}I=\int {\frac {x^{2n}}{2^{n}}}e^{-ax^{2}/2}dx={\frac {1\cdot 3\cdot 5\ldots \cdot (2n-1)}{2\cdot 2\cdot 2\ldots \;\;\;\;\;\cdot 2\;\;\;\;\;\;}}{\sqrt {2\pi }}\,a^{-{\frac {2n+1}{2}}}$

Dividing by I,

$\left\langle x^{2n}\right\rangle ={\frac {\displaystyle \int x^{2n}e^{-ax^{2}/2}}{\displaystyle \int e^{-ax^{2}/2}}}=1\cdot 3\cdot 5\ldots \cdot (2n-1){\frac {1}{a^{n}}}$

$\left\langle x^{2}\right\rangle ={\frac {1}{a}}$

If Wick's theorem were correct, the higher moments would be given by all possible pairings of a list of 2*n* different x:

$\left\langle x_{1}x_{2}x_{3}\cdots x_{2n}\right\rangle$

where the x are all the same variable, the index is just to keep track of the number of ways to pair them. The first x can be paired with 2*n* − 1 others, leaving 2*n* − 2. The next unpaired x can be paired with 2*n* − 3 different x leaving 2*n* − 4, and so on. This means that Wick's theorem, uncorrected, says that the expectation value of *x*2*n* should be:

$\left\langle x^{2n}\right\rangle =(2n-1)\cdot (2n-3)\ldots \cdot 5\cdot 3\cdot 1\left\langle x^{2}\right\rangle ^{n}$

and this is in fact the correct answer. So Wick's theorem holds no matter how many of the momenta of the internal variables coincide.

#### Interaction

Interactions are represented by higher order contributions, since quadratic contributions are always Gaussian. The simplest interaction is the quartic self-interaction, with an action:

$S=\int \partial ^{\mu }\phi \partial _{\mu }\phi +{\frac {\lambda }{4!}}\phi ^{4}.$

The reason for the combinatorial factor 4! will be clear soon. Writing the action in terms of the lattice (or continuum) Fourier modes:

$S=\int _{k}k^{2}\left|\phi (k)\right|^{2}+{\frac {\lambda }{4!}}\int _{k_{1}k_{2}k_{3}k_{4}}\phi (k_{1})\phi (k_{2})\phi (k_{3})\phi (k_{4})\delta (k_{1}+k_{2}+k_{3}+k_{4})=S_{F}+X.$

Where SF is the free action, whose correlation functions are given by Wick's theorem. The exponential of S in the path integral can be expanded in powers of λ, giving a series of corrections to the free action.

$e^{-S}=e^{-S_{F}}\left(1+X+{\frac {1}{2!}}XX+{\frac {1}{3!}}XXX+\cdots \right)$

The path integral for the full action is then a power series of corrections to the free action. The term represented by X should be thought of as four half-lines, one for each factor of *φ*(*k*). The half-lines meet at a vertex, which contributes a delta-function that ensures that the sum of the momenta are all equal.

To compute a correlation function in the interacting theory, there is a contribution from the X terms now. For example, the path-integral for the four-field correlator:

$\left\langle \phi (k_{1})\phi (k_{2})\phi (k_{3})\phi (k_{4})\right\rangle ={\frac {\displaystyle \int e^{-S}\phi (k_{1})\phi (k_{2})\phi (k_{3})\phi (k_{4})D\phi }{Z}}$

which in the free field was only nonzero when the momenta k were equal in pairs, is now nonzero for all values of k. The momenta of the insertions *φ*(*ki*) can now match up with the momenta of the Xs in the expansion. The insertions should also be thought of as half-lines, four in this case, which carry a momentum k, but one that is not integrated.

The lowest-order contribution comes from the first nontrivial term *e*−*SF**X* in the Taylor expansion of the action. Wick's theorem requires that the momenta in the X half-lines, the *φ*(*k*) factors in X, should match up with the momenta of the external half-lines in pairs. The new contribution is equal to:

$\lambda {\frac {1}{k_{1}^{2}}}{\frac {1}{k_{2}^{2}}}{\frac {1}{k_{3}^{2}}}{\frac {1}{k_{4}^{2}}}\,.$

The 4! inside X is canceled because there are exactly 4! ways to match the half-lines in X to the external half-lines. Each of these different ways of matching the half-lines together in pairs contributes exactly once, regardless of the values of *k*1,2,3,4, by Wick's theorem.

#### Feynman diagrams

The expansion of the action in powers of X gives a series of terms with progressively higher number of Xs. The contribution from the term with exactly n Xs is called nth order.

The nth order terms has:

1. 4*n* internal half-lines, which are the factors of *φ*(*k*) from the Xs. These all end on a vertex, and are integrated over all possible k.
2. external half-lines, which are the come from the *φ*(*k*) insertions in the integral.

By Wick's theorem, each pair of half-lines must be paired together to make a *line*, and this line gives a factor of

${\frac {\delta (k_{1}+k_{2})}{k_{1}^{2}}}$

which multiplies the contribution. This means that the two half-lines that make a line are forced to have equal and opposite momentum. The line itself should be labelled by an arrow, drawn parallel to the line, and labeled by the momentum in the line k. The half-line at the tail end of the arrow carries momentum k, while the half-line at the head-end carries momentum −*k*. If one of the two half-lines is external, this kills the integral over the internal k, since it forces the internal k to be equal to the external k. If both are internal, the integral over k remains.

The diagrams that are formed by linking the half-lines in the Xs with the external half-lines, representing insertions, are the Feynman diagrams of this theory. Each line carries a factor of ⁠1/*k*2⁠, the propagator, and either goes from vertex to vertex, or ends at an insertion. If it is internal, it is integrated over. At each vertex, the total incoming k is equal to the total outgoing k.

The number of ways of making a diagram by joining half-lines into lines almost completely cancels the factorial factors coming from the Taylor series of the exponential and the 4! at each vertex.

#### Loop order

A forest diagram is one where all the internal lines have momentum that is completely determined by the external lines and the condition that the incoming and outgoing momentum are equal at each vertex. The contribution of these diagrams is a product of propagators, without any integration. A tree diagram is a connected forest diagram.

An example of a tree diagram is the one where each of four external lines end on an X. Another is when three external lines end on an X, and the remaining half-line joins up with another X, and the remaining half-lines of this X run off to external lines. These are all also forest diagrams (as every tree is a forest); an example of a forest that is not a tree is when eight external lines end on two Xs.

It is easy to verify that in all these cases, the momenta on all the internal lines is determined by the external momenta and the condition of momentum conservation in each vertex.

A diagram that is not a forest diagram is called a *loop* diagram, and an example is one where two lines of an X are joined to external lines, while the remaining two lines are joined to each other. The two lines joined to each other can have any momentum at all, since they both enter and leave the same vertex. A more complicated example is one where two Xs are joined to each other by matching the legs one to the other. This diagram has no external lines at all.

The reason loop diagrams are called loop diagrams is because the number of k-integrals that are left undetermined by momentum conservation is equal to the number of independent closed loops in the diagram, where independent loops are counted as in homology theory. The homology is real-valued (actually **R***d* valued), the value associated with each line is the momentum. The boundary operator takes each line to the sum of the end-vertices with a positive sign at the head and a negative sign at the tail. The condition that the momentum is conserved is exactly the condition that the boundary of the k-valued weighted graph is zero.

A set of valid k-values can be arbitrarily redefined whenever there is a closed loop. A closed loop is a cyclical path of adjacent vertices that never revisits the same vertex. Such a cycle can be thought of as the boundary of a hypothetical 2-cell. The k-labellings of a graph that conserve momentum (i.e. which has zero boundary) up to redefinitions of k (i.e. up to boundaries of 2-cells) define the first homology of a graph. The number of independent momenta that are not determined is then equal to the number of independent homology loops. For many graphs, this is equal to the number of loops as counted in the most intuitive way.

#### Symmetry factors

The number of ways to form a given Feynman diagram by joining half-lines is large, and by Wick's theorem, each way of pairing up the half-lines contributes equally. Often, this completely cancels the factorials in the denominator of each term, but the cancellation is sometimes incomplete.

The uncancelled denominator is called the *symmetry factor* of the diagram. The contribution of each diagram to the correlation function must be divided by its symmetry factor.

For example, consider the Feynman diagram formed from two external lines joined to one X, and the remaining two half-lines in the X joined to each other. There are 4 × 3 ways to join the external half-lines to the X, and then there is only one way to join the two remaining lines to each other. The X comes divided by 4! = 4 × 3 × 2, but the number of ways to link up the X half lines to make the diagram is only 4 × 3, so the contribution of this diagram is divided by two.

For another example, consider the diagram formed by joining all the half-lines of one X to all the half-lines of another X. This diagram is called a *vacuum bubble*, because it does not link up to any external lines. There are 4! ways to form this diagram, but the denominator includes a 2! (from the expansion of the exponential, there are two Xs) and two factors of 4!. The contribution is multiplied by ⁠4!/2 × 4! × 4!⁠ = ⁠1/48⁠.

Another example is the Feynman diagram formed from two Xs where each X links up to two external lines, and the remaining two half-lines of each X are joined to each other. The number of ways to link an X to two external lines is 4 × 3, and either X could link up to either pair, giving an additional factor of 2. The remaining two half-lines in the two Xs can be linked to each other in two ways, so that the total number of ways to form the diagram is 4 × 3 × 4 × 3 × 2 × 2, while the denominator is 4! × 4! × 2!. The total symmetry factor is 2, and the contribution of this diagram is divided by 2.

The symmetry factor theorem gives the symmetry factor for a general diagram: the contribution of each Feynman diagram must be divided by the order of its group of automorphisms, the number of symmetries that it has.

An automorphism of a Feynman graph is a permutation M of the lines and a permutation N of the vertices with the following properties:

1. If a line l goes from vertex v to vertex v′, then *M*(*l*) goes from *N*(*v*) to *N*(*v′*). If the line is undirected, as it is for a real scalar field, then *M*(*l*) can go from *N*(*v′*) to *N*(*v*) too.
2. If a line l ends on an external line, *M*(*l*) ends on the same external line.
3. If there are different types of lines, *M*(*l*) should preserve the type.

This theorem has an interpretation in terms of particle-paths: when identical particles are present, the integral over all intermediate particles must not double-count states that differ only by interchanging identical particles.

Proof: To prove this theorem, label all the internal and external lines of a diagram with a unique name. Then form the diagram by linking a half-line to a name and then to the other half line.

Now count the number of ways to form the named diagram. Each permutation of the Xs gives a different pattern of linking names to half-lines, and this is a factor of *n*!. Each permutation of the half-lines in a single X gives a factor of 4!. So a named diagram can be formed in exactly as many ways as the denominator of the Feynman expansion.

But the number of unnamed diagrams is smaller than the number of named diagram by the order of the automorphism group of the graph.

#### Connected diagrams: *linked-cluster theorem*

Roughly speaking, a Feynman diagram is called *connected* if all vertices and propagator lines are linked by a sequence of vertices and propagators of the diagram itself. If one views it as an undirected graph it is connected. The remarkable relevance of such diagrams in QFTs is due to the fact that they are sufficient to determine the quantum partition function *Z*[*J*]. More precisely, connected Feynman diagrams determine

$iW[J]\equiv \ln Z[J].$

To see this, one should recall that

$Z[J]\propto \sum _{k}{D_{k}}$

with Dk constructed from some (arbitrary) Feynman diagram that can be thought to consist of several connected components Ci. If one encounters ni (identical) copies of a component Ci within the Feynman diagram Dk one has to include a *symmetry factor* *ni*!. However, in the end each contribution of a Feynman diagram Dk to the partition function has the generic form

$\prod _{i}{\frac {C_{i}^{n_{i}}}{n_{i}!}}$

where i labels the (infinitely) many connected Feynman diagrams possible.

A scheme to successively create such contributions from the Dk to *Z*[*J*] is obtained by

$\left({\frac {1}{0!}}+{\frac {C_{1}}{1!}}+{\frac {C_{1}^{2}}{2!}}+\cdots \right)\left(1+C_{2}+{\frac {1}{2}}C_{2}^{2}+\cdots \right)\cdots$

and therefore yields

$Z[J]\propto \prod _{i}{\sum _{n_{i}=0}^{\infty }{\frac {C_{i}^{n_{i}}}{n_{i}!}}}=\exp {\sum _{i}{C_{i}}}\propto \exp {W[J]}\,.$

To establish the *normalization* *Z*0 = exp *W*[0] = 1 one simply calculates all connected *vacuum diagrams*, i.e., the diagrams without any *sources* J (sometimes referred to as *external legs* of a Feynman diagram).

The linked-cluster theorem was first proved to order four by Keith Brueckner in 1955, and for infinite orders by Jeffrey Goldstone in 1957.

#### Vacuum bubbles

An immediate consequence of the linked-cluster theorem is that all vacuum bubbles, diagrams without external lines, cancel when calculating correlation functions. A correlation function is given by:

$\left\langle \phi _{1}(x_{1})\cdots \phi _{n}(x_{n})\right\rangle ={\frac {\displaystyle \int e^{-S}\phi _{1}(x_{1})\cdots \phi _{n}(x_{n})\,D\phi }{\displaystyle \int e^{-S}\,D\phi }}\,.$

The numerator is the sum over all Feynman diagrams, including disconnected diagrams that do not link up to external lines at all. In terms of the connected diagrams, the numerator includes the same contributions of vacuum bubbles as the denominator:

$\int e^{-S}\phi _{1}(x_{1})\cdots \phi _{n}(x_{n})\,D\phi =\left(\sum E_{i}\right)\left(\exp \left(\sum _{i}C_{i}\right)\right)\,.$

Where the sum over E diagrams includes only those diagrams each of whose connected components end on at least one external line. The vacuum bubbles are the same whatever the external lines, and give an overall multiplicative factor. The denominator is the sum over all vacuum bubbles, and dividing gets rid of the second factor.

The vacuum bubbles then are only useful for determining Z itself, which from the definition of the path integral is equal to:

$Z=\int e^{-S}D\phi =e^{-HT}=e^{-\rho V}$

where ρ is the energy density in the vacuum. Each vacuum bubble contains a factor of *δ*(*k*) zeroing the total k at each vertex, and when there are no external lines, this contains a factor of *δ*(0), because the momentum conservation is over-enforced. In finite volume, this factor can be identified as the total volume of space time. Dividing by the volume, the remaining integral for the vacuum bubble has an interpretation: it is a contribution to the energy density of the vacuum.
