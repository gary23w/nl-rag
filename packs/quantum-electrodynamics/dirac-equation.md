---
title: "Dirac equation"
source: https://en.wikipedia.org/wiki/Dirac_equation
domain: quantum-electrodynamics
license: CC-BY-SA-4.0
tags: quantum electrodynamics, vacuum polarization, compton scattering, dirac equation
fetched: 2026-07-02
---

# Dirac equation

In particle physics, the **Dirac equation** is a relativistic wave equation derived by British physicist Paul Dirac in 1928. In its free form, or including electromagnetic interactions, it describes all spin-⁠1/2⁠ massive particles, called "Dirac particles", such as electrons and quarks for which parity is a symmetry. It is consistent with both the principles of quantum mechanics and the theory of special relativity, and was the first theory to fully account for special relativity in the context of quantum mechanics. The equation is validated by its rigorous accounting of the observed fine structure of the hydrogen spectrum and has become vital in the building of the Standard Model.

The equation also implied the existence of a new form of matter, *antimatter*, previously unsuspected and unobserved. The existence of antimatter was experimentally confirmed several years later. It also provided a *theoretical* justification for the introduction of several component wave functions in Pauli's phenomenological theory of spin. The wave functions in the Dirac theory are vectors of four complex numbers (known as Dirac spinors), two of which resemble the Pauli wavefunction in the non-relativistic limit, in contrast to the Schrödinger equation, which described wave functions of only one complex value. Moreover, in the limit of zero mass, the Dirac equation reduces to the Weyl equation. In the context of quantum field theory, the Dirac equation is reinterpreted to describe quantum fields corresponding to spin-⁠1/2⁠ particles.

Dirac did not fully appreciate the importance of his results; however, the entailed explanation of spin as a consequence of the union of quantum mechanics and relativity—and the eventual discovery of the positron—represents one of the great triumphs of theoretical physics. This accomplishment has been described as fully on par with the works of Isaac Newton, James Clerk Maxwell, and Albert Einstein before him. The equation has been deemed by some physicists to be "the real seed of modern physics". The Dirac equation has been described as the "centerpiece of relativistic quantum mechanics", and as "perhaps the most important [equation] in all of quantum mechanics".

## History

### Early attempts at a relativistic formulation

The first phase in the development of quantum mechanics, lasting between 1900 and 1925, focused on explaining individual phenomena that could not be explained through classical mechanics. The second phase, starting in the mid-1920s, saw the development of two systematic frameworks governing quantum mechanics. The first, known as matrix mechanics, uses matrices to describe physical observables; it was developed in 1925 by Werner Heisenberg, Max Born, and Pascual Jordan. The second, known as wave mechanics, uses a wave equation known as the Schrödinger equation to describe the state of a system; it was developed the next year by Erwin Schrödinger. While these two frameworks were initially seen as competing approaches, they would later be shown to be equivalent.

Both these frameworks only formulated quantum mechanics in a non-relativistic setting. This was seen as a deficiency right from the start, with Schrödinger originally attempting to formulate a relativistic version of the Schrödinger equation, in the process discovering the Klein–Gordon equation. However, after showing that this equation did not correctly reproduce the relativistic corrections to the hydrogen atom spectrum for which an exact form was known due to Arnold Sommerfeld, he abandoned his relativistic formulation. The Klein–Gordon equation was also found by at least six other authors in the same year.

During 1926 and 1927, there was a widespread effort to incorporate relativity into quantum mechanics, largely through two approaches. The first was to consider the Klein–Gordon as the correct relativistic generalization of the Schrödinger equation. Such an approach was viewed unfavourably by many leading theorists since it failed to correctly predict numerous experimental results, and more importantly it appeared difficult to reconcile with the principles of quantum mechanics as understood at the time. These conceptual issues primarily arose due to the presence of a second temporal derivative.

The second approach introduced relativistic effects as corrections to the known non-relativistic formulas. This provided many provisional answers that were expected to eventually be supplanted by some yet-unknown relativistic formulation of quantum mechanics. One notable result by Heisenberg and Jordan was the introduction of two terms for spin and relativity into the hydrogen Hamiltonian, allowing them to derive the first-order approximation of the Sommerfeld fine structure formula.

A parallel development during this time was the concept of spin, first introduced in 1925 by Samuel Goudsmit and George Uhlenbeck. Shortly after, it was conjectured by Schrödinger to be the missing link in acquiring the correct Sommerfeld formula. In 1927, Wolfgang Pauli used the ideas of spin to find an effective theory for a nonrelativistic spin-⁠1/2⁠ particle, the Pauli equation. He did this by taking the Schrödinger equation and, rather than just assuming that the wave function depends on the physical coordinate, he also assumed that it depends on a spin coordinate that can take only two values $\pm {\tfrac {\hbar }{2}}$ . While this was still a non-relativistic formulation, he believed that a fully relativistic formulation possibly required a more complicated model for the electron, one that moved beyond a point particle.

### Dirac's relativistic quantum mechanics

By 1927, many physicists no longer considered the fine structure of hydrogen as a crucial puzzle that called for a completely new relativistic formulation since it could effectively be solved using the Pauli equation or by introducing a spin-⁠1/2⁠ angular momentum quantum number in the Klein–Gordon equation. At the fifth Solvay Conference held that year, Paul Dirac was primarily concerned with the logical development of quantum mechanics. However, he realized that many other physicists complacently accepted the Klein–Gordon equation as a satisfactory relativistic formulation, which demanded abandoning basic principles of quantum mechanics as understood at the time, to which Dirac strongly objected. After his return from Brussels, Dirac focused on finding a relativistic theory for electrons. Within two months he solved the problem and published his results on January 2, 1928.

In his paper, Dirac was guided by two principles from transformation theory, the first being that the equation should be invariant under transformations of special relativity, and the second that it should transform under the transformation theory of quantum mechanics. The latter demanded that the equation would have to be linear in temporal derivatives, so that it would admit a probabilistic interpretation. His argument begins with the Klein–Gordon equation

$\left[{\boldsymbol {p}}^{2}+m^{2}c^{2}\right]\phi (t,x)=-{\frac {\hbar ^{2}}{c^{2}}}{\frac {\partial ^{2}}{\partial t^{2}}}\phi (t,x),$

describing a particle using the wave function $\phi (t,x)$ . Here ${\boldsymbol {p}}^{2}=p_{1}^{2}+p_{2}^{2}+p_{3}^{2}$ is the square of the momentum, m is the rest mass of the particle, c is the speed of light, and $\hbar$ is the reduced Planck constant. The naive way to get an equation linear in the time derivative is to essentially consider the square root of both sides. This replaces ${\boldsymbol {p}}^{2}+m^{2}c^{2}$ with ${\sqrt {{\boldsymbol {p}}^{2}+m^{2}c^{2}}}$ . However, such a square root is mathematically problematic for the resulting theory, making it unfeasible.

Dirac's first insight was the concept of linearization. He looked for some sort of variables $\alpha _{i}$ that are independent of momentum and spacetime coordinates for which the square root could be rewritten in a linear form

${\sqrt {p_{1}^{2}+p_{2}^{2}+p_{3}^{2}+(mc)^{2}}}=\alpha _{1}p_{1}+\alpha _{2}p_{2}+\alpha _{3}p_{3}+\alpha _{4}mc.$

By squaring this operator and demanding that it reduces to the Klein–Gordon equation, Dirac found that the variables must satisfy $\alpha _{i}^{2}=1$ and $\alpha _{i}\alpha _{j}+\alpha _{j}\alpha _{i}=0$ if $i\neq j$ . Dirac initially considered the $2\times 2$ Pauli matrices as a candidate, but then showed these would not work since it is impossible to find a set of four $2\times 2$ matrices that all anticommute with each other. His second insight was to instead consider four-dimensional matrices. In that case the equation would be acting on a four-component wavefunction $\psi =(\psi _{1},\psi _{2},\psi _{3},\psi _{4})$ . Such a proposal was much more bold than Pauli's original generalization to a two-component wavefunction in the Pauli equation. This is because in Pauli's case, this was motivated by the demand to encode the two spin states of the particle. In contrast, Dirac had no physical argument for a four-component wavefunction, but instead introduced it as a matter of mathematical necessity. He thus arrived at the Dirac equation

$(\alpha _{1}p_{1}+\alpha _{2}p_{2}+\alpha _{3}p_{3}+\alpha _{4}mc)\psi (t,x)=i{\frac {\hbar }{c}}{\frac {\partial }{\partial t}}\psi (t,x).$

Dirac constructed the correct matrices $\alpha _{i}$ without realizing that they form a mathematical structure known of since the early 1880s, the Clifford algebra. By recasting the equation in a Lorentz invariant form, he also showed that it correctly combines special relativity with his principle of quantum mechanical transformation theory, making it a viable candidate for a relativistic theory of the electron.

To investigate the equation further, he examined how it behaves in the presence of an electromagnetic field. To his surprise, this showed that it described a particle with a magnetic moment arising due to the particle having spin ⁠1/2⁠. Spin directly emerged from the equation, without Dirac having added it in by hand. Additionally, he focused on showing that the equation successfully reproduces the fine structure of the hydrogen atom, at least to first order. The equation therefore succeeds where all previous attempts have failed, in correctly describing relativistic phenomena of electrons from first principles rather than through the ad hoc modification of existing formulas.

### Consequences

Except for his followup paper deriving the Zeeman effect and Paschen–Back effect from the equation in the presences of a magnetic fields, Dirac left the work of examining the consequences of his equation to others, and only came back to the subject in 1930. Once the equation was published, it was recognized as the correct solution to the problem of spin, relativity, and quantum mechanics. At first the Dirac equation was considered the only valid relativistic equation for a particle with mass. Then in 1934 Pauli and Victor Weisskopf reinterpreted the Klein–Gordon equation as the equation for a relativistic spinless particle.

One of the first calculations was to reproduce the Sommerfeld fine structure formula exactly, which was performed independently by Charles Galton Darwin and Walter Gordon in 1928. This is the first time that the full formula has been derived from first principles. Further work on the mathematics of the equation was undertaken by Hermann Weyl in 1929. In this work he showed that the massless Dirac equation can be decomposed into a pair of Weyl equations.

The Dirac equation was also used to study various scattering processes. In particular, the Klein–Nishina formula, looking at photon-electron scattering, was also derived in 1928. Mott scattering, the scattering of electrons off a heavy target such as atomic nuclei, followed the next year. Over the following years it was further used to derive other standard scattering processes such as Moller scattering in 1932 and Bhabha scattering in 1936.

A problem that gained more focus with time was the presence of negative energy states in the Dirac equation, which led to many efforts to try to eliminate such states. Dirac initially simply rejected the negative energy states as unphysical, but the problem was made more clear when in 1929 Oskar Klein showed that in static fields there exists inevitable mixing between the negative and positive energy states. Dirac's initial response was to believe that his equation must have some sort of defect, and that it was only the first approximation of a future theory that would not have this problem. However, he then suggested a solution to the problem in the form of the Dirac sea. This is the idea that the universe is filled with an infinite sea of negative energy electrons states. Positive energy electron states then live in this sea and are prevented from decaying to the negative energy states through the Pauli exclusion principle.

Additionally, Dirac postulated the existence of positively charged holes in the Dirac sea, which he initially suggested could be the proton. However, Oppenheimer showed that in this case stable atoms could not exist and Weyl further showed that the holes would have to have the same mass as the electrons. Persuaded by Oppenheimer's and Weyl's argument, Dirac published a paper in 1931 that predicted the existence of an as-yet-unobserved particle that he called an "anti-electron" that would have the same mass and the opposite charge as an electron and that would mutually annihilate upon contact with an electron. He suggested that every particle may have an oppositely charged partner, a concept now called antimatter

In 1933 Carl Anderson discovered the "positive electron", now called a positron, which had all the properties of Dirac's anti-electron. While the Dirac sea was later superseded by quantum field theory, its conceptual legacy survived in the idea of a dynamical vacuum filled with virtual particles. In 1949 Ernst Stueckelberg suggested and Richard Feynman showed in detail that the negative energy solutions can be interpreted as particles traveling backwards in proper time. The concept of the Dirac sea is also realized more explicitly in some condensed matter systems in the form of the Fermi sea, which consists of a sea of filled valence electrons below some chemical potential.

Significant work was done over the following decades to try to find spectroscopic discrepancies compared to the predictions made by the Dirac equation, however it was not until 1947 that Lamb shift was discovered, which the equation does not predict. This led to the development of quantum electrodynamics in 1950s, with the Dirac equation then being incorporated within the context of quantum field theory. Since it describes the dynamics of Dirac spinors, it went on to play a fundamental role in the Standard Model as well as many other areas of physics. For example, within condensed matter physics, systems whose fermions have a near linear dispersion relation are described by the Dirac equation. Such systems are known as Dirac matter and they include graphene and topological insulators, which have become a major area of research since the start of the 21st century.

The Dirac equation is inscribed upon a plaque on the floor of Westminster Abbey. Unveiled on 13 November 1995, the plaque commemorates Dirac's life. The equation, in its natural units formulation, is also prominently displayed in the auditorium at the ‘Paul A.M. Dirac’ Lecture Hall at the Patrick M.S. Blackett Institute (formerly The San Domenico Monastery) of the Ettore Majorana Foundation and Centre for Scientific Culture in Erice, Sicily.

## Formulation

### Covariant formulation

In its modern field theoretic formulation, the Dirac equation in 3+1 dimensional Minkowski spacetime is written in terms of a *Dirac field* $\psi (x)$ . This is a field that assigns a complex vector from $\mathbb {C} ^{4}$ to each point in spacetime, where the key property of the field is that it transforms as a Dirac spinor under Lorentz transformations. In natural units where $\hbar =c=1$ , the Lorentz covariant formulation of the Dirac equation is given by

Dirac equation

$(i{{\partial }\!\!\!/}-m)\psi (x)=0,$

where ${{\partial }\!\!\!/}=\gamma ^{\mu }\partial _{\mu }$ is a contraction between the four-gradient $\partial _{\mu }$ and the gamma matrices $\gamma ^{\mu }$ . These are a set of four matrices generating the Dirac algebra, which requires them to satisfy

$\{\gamma ^{\mu },\gamma ^{\nu }\}=2\eta ^{\mu \nu }I_{4},$

where $\{a,b\}=ab+ba$ is the anticommutator, $\eta ^{\mu \nu }$ is the Minkowski metric in a mainly negative signature, and $I_{4}$ is the $4\times 4$ identity matrix. The Dirac algebra is a special case of the more general mathematical structure known as a Clifford algebra. The Dirac algebra can also be seen as the real part of the spacetime algebra. There is no unique choice of matrices for the gamma matrices, with different choices known as different representations of the algebra. One common choice, originally discovered by Dirac, is known as the Dirac representation. Here the matrices are given by

$\gamma ^{0}={\begin{pmatrix}I_{2}&0\\0&-I_{2}\end{pmatrix}},\qquad \gamma ^{i}={\begin{pmatrix}0&\sigma _{i}\\-\sigma _{i}&0\end{pmatrix}},$

where $\sigma _{i}$ are the three Pauli matrices for $i\in \{1,2,3\}$ . There are two other common representations for the gamma matrices. The first is the chiral representation, which is useful when decomposing the Dirac equation into a pair of Weyl equations. The second is the Majorana representation, for which all gamma matrices are imaginary, so the Dirac operator is purely real. This representation is useful for studying Majorana spinors, which are purely real four-component spinor solutions of the Dirac equation.

By taking the hermitian conjugate of the Dirac equation and multiplying it by $\gamma ^{0}$ from the right, the adjoint Dirac equation can be found, with this being the equation of motion for the Dirac adjoint ${\bar {\psi }}=\psi ^{\dagger }\gamma ^{0}$ . It is given by

${\bar {\psi }}(x)(-i\gamma ^{\mu }{\overleftarrow {\partial }}_{\mu }-m)=0.$

The adjoint spinor is useful in forming Lorentz invariant quantities. For example, the bilinear $\psi ^{\dagger }\psi$ is not Lorentz invariant, but ${\bar {\psi }}\psi$ is. Here ${\overleftarrow {\partial }}_{\mu }$ is shorthand notation for a partial derivative acting on the left. In regular notation, the adjoint Dirac equation is equivalent to

$-i\partial _{\mu }{\bar {\psi }}(x)\gamma ^{\mu }-m{\bar {\psi }}(x)=0.$

The Dirac equation can be rewritten in a non-covariant form similar to that of the Schrödinger equation

$i\hbar {\frac {\partial }{\partial t}}\psi (t,{\boldsymbol {x}})=-i\hbar c{\boldsymbol {\alpha }}\cdot {\boldsymbol {\nabla }}\psi (t,{\boldsymbol {x}})+\beta mc^{2}\psi (t,{\boldsymbol {x}}).$

The right-hand side of the equation is the Hamiltonian acting on the Dirac spinor $H\psi$ . Here ${\boldsymbol {\alpha }}$ and $\beta$ are a set of four Hermitian $4\times 4$ matrices that all anticommute with each other and square to the identity. They are related to the gamma matrices through $\gamma ^{0}=\beta$ and $\gamma ^{i}=\beta \alpha _{i}$ . This form is useful in quantum mechanics, where the Hamiltonian can be easily modified to solve a wide range of problems, such as by introducing a potential or through a minimal coupling to the electromagnetic field.

### Dirac action

The Dirac equation can also be acquired from a Lagrangian formulation of the field theory, where the Dirac action is given by

$S=\int d^{4}x{\bar {\psi }}(i{{\partial }\!\!\!/}-m)\psi .$

The equation then arises as the Euler–Lagrange equation of this action, found by varying the adjoint spinor ${\bar {\psi }}(x)$ . Meanwhile, the adjoint Dirac equation is acquired by varying the spinor $\psi (x)$ . The action formulation of the Dirac equation has the advantage of making the symmetries of the Dirac equation more explicit, since they leave its action invariant. Noether's theorem then allows for the direct calculation of currents corresponding to these symmetries. Additionally, the action is usually used to define the associated quantum field theory, such as through the path integral formulation.

### Meaning of the Dirac fields

In quantum mechanics, the Dirac spinor $\psi (x)$ corresponds to a four-component spinor wave function describing the state of a Dirac fermion. Its position probability density, the probability of finding the fermion in a region of space, is described by the zeroth component of its vector current, $\psi ^{\dagger }\psi$ . In the case of a large number of particles, it can also be interpreted as the charge density. An appropriate normalization is required to ensure that the total probability across all of space is equal to one, with probability conservation following directly from the conservation of the vector current. The Dirac equation is the relativistic analogue of the Schrödinger equation for the Dirac fermion wavefunction.

In the second quantization form of quantum field theory the Dirac spinor is quantized to be an operator-valued spinor field ${\hat {\psi }}(x)$ . In contrast to quantum mechanics, it no longer represents the state in the Hilbert space, but is rather the operator that acts on states to create or destroy particles. Observables are formed using expectation values of these operators. The Dirac equation then becomes an operator equation describing the state-independent evolution of the operator-valued spinor field

$(i{{\partial }\!\!\!/}-m){\hat {\psi }}(x)=0.$

In the path integral formulation of quantum field theory, the spinor field $\psi (x)$ is an anti-commuting Grassmann-valued field that only acts as an integration variable. The Dirac equation then emerges as the classical saddle point behaviour of the path integral. It also arises as an equation of the expectation value of the classical field variables

$\langle (i{{\partial }\!\!\!/}-m)\psi (x)\rangle =0,$

in the sense of the Schwinger–Dyson equations. This version of the equation can also be acquired by taking the expectation value of the operator equation.

The Dirac equation also arises in describing the time evolution of a spinor field in classical field theory. Such a field theory would have the special linear group ${\text{SL}}(2,\mathbb {C} )$ as its spacetime symmetry group rather than the Lorentz group, since the latter does not admit spinor representations. This is in contrast to the quantum theory which does admit spinor representations even when the spacetime symmetries are described by the Lorentz group. This is because the states in a Hilbert space are defined only up to a complex phase, so particles belong to projective representations rather than regular representations, with the projective representations of the Lorentz group being equivalent to regular representations of ${\text{SL}}(2,\mathbb {C} )$ . Classical spinor fields do not arise in our universe because the Pauli exclusion principle prevents populating the field with a sufficient number of particles to reach the classical limit.

## Properties

### Lorentz transformations

The Lorentz group ${\text{SO}}(1,3)$ , describing the transformation between inertial reference frames, can admit many different representations. A representation is a particular choice of matrices that faithfully represent the action of the group on some vector space, where the dimensionality of the matrices can differ between representations. For example, the Lorentz group can be represented by $4\times 4$ real matrices $\Lambda$ acting on the vector space $\mathbb {R} ^{1,3}$ , corresponding to how Lorentz transformations act on vectors or on spacetime. Another representation is a set of $4\times 4$ complex matrices acting on Dirac spinors in the complex vector space $\mathbb {C} ^{4}$ . A smaller representation is a set of $2\times 2$ complex matrices acting on Weyl spinors in the $\mathbb {C} ^{2}$ vector space.

Lie group elements can be generated using the corresponding Lie algebra, which together with a Lie bracket, describes the tangent space of the group manifold around its identity element. The basis elements of this vector space are known as generators of the group. A particular group element is then acquired by exponentiating a corresponding tangent space vector. The generators of the Lorentz Lie algebra must satisfy certain anticommutation relations, known as a Lie bracket. The six vectors can be packaged into an antisymmetric object $X^{\mu \nu }$ indexed by $\{\mu ,\nu \}$ , with the bracket for the Lorentz algebra given by

$[X^{\mu \nu },X^{\rho \sigma }]=i(\eta ^{\nu \rho }X^{\mu \sigma }-\eta ^{\mu \rho }X^{\nu \sigma }+\eta ^{\mu \sigma }X^{\nu \rho }-\eta ^{\nu \sigma }X^{\mu \rho }).$

This algebra admits numerous representation, where each generator is represented by a matrix, with each algebra representation generating a corresponding representation of the group. For example, the representation acting on real vectors is given by the six matrices $X^{\mu \nu }=M^{\mu \nu }$ where

$\left(M^{\mu \nu }\right)^{\rho }{}_{\sigma }=i(\eta ^{\mu \rho }\delta ^{\nu }{}_{\sigma }-\eta ^{\nu \rho }\delta ^{\mu }{}_{\sigma }).$

The Lorentz transformation matrix can then be acquired from these generators through an exponentiation

$\Lambda =\exp \left({\tfrac {i}{2}}\omega _{\mu \nu }M^{\mu \nu }\right),$

where $\omega _{\mu \nu }$ is an antisymmetric matrix encoding the six degrees of freedom of the Lorentz group used to specify the particular group element. These correspond to the three boosts and three rotations.

Another representation for the Lorentz algebra is the spinor representation where the generators are given by

$S^{\mu \nu }={\tfrac {i}{4}}[\gamma ^{\mu },\gamma ^{\nu }].$

In this case the Lorentz group element, specified by $\omega _{\mu \nu }$ , is given by

$S[\Lambda ]=\exp \left({\tfrac {i}{2}}\omega _{\mu \nu }S^{\mu \nu }\right).$

The mapping of $\Lambda \mapsto S[\Lambda ]$ is not one-to-one since there are two consistent choices for $\omega _{\mu \nu }$ that give the same $\Lambda$ but a different $S[\Lambda ]$ . This is a consequence of the spinor representation being projective representations of the Lorentz group ${\text{SO}}(1,3)$ . Equivalently, they are regular representation of ${\text{SL}}(2,\mathbb {C} )$ , which is a double cover of the Lorentz group.

Under a Lorentz transformation, spacetime coordinates transform under the vector representation $x'^{\mu }=\Lambda ^{\mu }{}_{\nu }x^{\nu }$ , while the spinors transform under the spinor representation

$\psi '(x')=S[\Lambda ]\psi (x).$

The Dirac equation is a Lorentz covariant equation, meaning that it takes the form in all inertial reference frames. That is, it takes the same form when for a spinor $\psi (x)$ with coordinates x , as well as for a Lorentz transformed spinor $\psi '(x')$ in the Lorentz transformed coordinates $x'=\Lambda x$

$(i{{\partial }\!\!\!/}'-m)\psi '(x')=0,$

where $\partial _{\mu }'$ is the four-gradient for the new coordinates $x'$ . Meanwhile, the Dirac action is Lorentz invariant, meaning that it is the same in all reference frames $S'=S$ .

### Symmetries

Dirac's theory is invariant under a global ${\text{U}}(1)$ symmetry acting on the phase of the spinor

$\psi (x)\rightarrow e^{i\alpha }\psi (x),\qquad {\bar {\psi }}(x)\rightarrow e^{-i\alpha }{\bar {\psi }}(x).$

This has a corresponding conserved current that can be derived from the action using Noether's theorem, given by

$j^{\mu }={\bar {\psi }}\gamma ^{\mu }\psi .$

This symmetry is known as the vector symmetry because its current transforms as a vector under Lorentz transformations. Promoting this symmetry to a gauge symmetry gives rise to quantum electrodynamics.

In the massless limit, the Dirac equation has a second inequivalent ${\text{U}}(1)$ symmetry known as the axial symmetry, which acts on the spinors as

$\psi (x)\rightarrow e^{i\beta \gamma ^{5}}\psi (x),\qquad {\bar {\psi }}(x)\rightarrow e^{i\beta \gamma ^{5}}{\bar {\psi }}(x),$

where $\gamma _{5}$ is the chiral matrix. This arises because in the massless limit the Dirac equation reduces to a pair of Weyl equations. Each of these is invariant under a ${\text{U}}(1)$ phase symmetry. These two symmetries can then be grouped into the vector symmetry where both Weyl spinors transform by the same phase, and the axial symmetry where they transform under the opposite signs of the phase. The current corresponding to the axial symmetry is given by

$j_{5}^{\mu }={\bar {\psi }}\gamma ^{\mu }\gamma ^{5}\psi .$

This transforms as a pseudovector, meaning that its spatial part is odd under parity transformations. Classically, the axial symmetry admits a well-formulated gauge theory, but at the quantum level it has a chiral anomaly that provides an obstruction towards gauging.

The spacetime symmetries of the Dirac action correspond to the Poincaré group, a combination of spacetime translations and the Lorentz group. Invariance under the four spacetime translations yields the Dirac stress-energy tensor as its four-currents

$T^{\mu \nu }=i{\bar {\psi }}\gamma ^{\mu }\partial ^{\nu }\psi -\eta ^{\mu \nu }{\mathcal {L}}_{\text{Dirac}},$

where the last term is the Dirac Lagrangian, which vanishes on shell. Invariance under Lorentz transformations meanwhile yields a set of currents indexed by $\rho$ and $\sigma$ , given by

$({\mathcal {J}}^{\mu })^{\rho \sigma }=x^{\rho }T^{\mu \sigma }-x^{\sigma }T^{\mu \rho }+{\bar {\psi }}\gamma ^{\mu }S^{\rho \sigma }\psi ,$

where $S^{\rho \sigma }$ are the spinor representation generators of the Lorentz Lie algebra, used to define how spinors transform under Lorentz transformations.

### Plane wave solutions

Acting on the Dirac equation with the operator $(i{{\partial }\!\!\!/}+m)$ gives rise to the Klein–Gordon equation for each component of the spinor

$(i{{\partial }\!\!\!/}+m)(i{{\partial }\!\!\!/}-m)\psi (x)=\left(\partial _{\mu }\partial ^{\mu }+m^{2}\right)\psi (x)=0.$

As a result, any solution to the Dirac equation is also automatically a solution to the Klein–Gordon equation. Its solutions can therefore be written as a linear combination of plane waves.

The Dirac equation admits positive frequency plane wave solutions

$\psi (x)=u({\boldsymbol {p}})e^{ip_{\mu }x^{\mu }}$

with a positive energy given by $p_{0}={\sqrt {{\boldsymbol {p}}^{2}+m^{2}}}>0$ . It also admits negative frequency solutions taking the same form except with $p_{0}=-{\sqrt {{\boldsymbol {p}}^{2}+m^{2}}}<0$ . It is more convenient to rewrite these negative frequency solutions by flipping the sign of the momentum to ensure that they have a positive energy $p_{0}>0$ and so take the form

$\psi (x)=v({\boldsymbol {p}})e^{-ip_{\mu }x^{\mu }}.$

At the classical level these are positive and negative frequency solutions to a classical wave equation, but in the quantum theory they correspond to operators creating particles with spinor polarization $u({\boldsymbol {p}})$ or annihilating antiparticles with spinor polarization $v({\boldsymbol {p}})$ . Both these spinor polarizations satisfy the momentum space Dirac equation

$({{p}\!\!\!/}+m)u({\boldsymbol {p}})=0,$

$({{p}\!\!\!/}-m)v({\boldsymbol {p}})=0.$

Since these are simple matrix equations, they can be solved directly once an explicit representation for the gamma matrices is chosen. In the chiral representation the general solution is given by

$u({\boldsymbol {p}})={{\sqrt {p\cdot \sigma }}\xi _{s} \choose {\sqrt {p\cdot {\bar {\sigma }}}}\xi _{s}},\qquad v({\boldsymbol {p}})={{\sqrt {p\cdot \sigma }}\eta _{s} \choose -{\sqrt {p\cdot {\bar {\sigma }}}}\eta _{s}},$

where $\xi _{s}$ and $\eta _{s}$ are arbitrary complex 2-vectors, describing the two spin degrees of freedom for the particle and two for the antiparticle. In the massless limit, these spin states correspond to the possible helicity states that the massless fermions can have, either being left-handed or right-handed.

While the standard Dirac equation was originally derived in a $3+1$ dimensional spacetime, it can be directly generalized to arbitrary dimension and metric signatures, where it takes the same covariant form. The crucial difference is that the gamma matrices must be changed to gamma matrices of the Clifford algebra appropriate in those dimensions and metric signature, with the size of the Dirac spinor corresponding to the dimensionality of the gamma matrices. While the Dirac equation always exists, since every dimension admits Dirac spinors, the properties of these spinors and their relation to other spinor representations differs significantly across dimensions. Other differences include the absence of a chirality matrix in odd dimensions.

The equation can also be generalized from flat Minkowski spacetime to curved spacetime through the introduction of a spinor covariant derivative

$D_{\mu }=\partial _{\mu }-{\tfrac {i}{4}}\left(\omega _{\alpha \beta }\right)_{\mu }\gamma ^{\alpha }\gamma ^{\beta },$

where $\omega _{\alpha \beta }$ is the spin connection that can be defined using the tetrad formalism. The Dirac equation in curved spacetime then takes the form

$(i\gamma ^{\mu }D_{\mu }-m)\psi (x)=0.$

Adding self-interaction terms to the Dirac action gives rise to the nonlinear Dirac equation, which allows for the fermions to interact with themselves, such as in the Thirring model. Interactions between fermions can also be introduced through electromagnetic effects. In particular, the Breit equation describes multi-electron systems interacting electromagnetically to first order in perturbation theory. The two-body Dirac equation is a similar multi-body equation.

A geometric reformulation of the Dirac equation is known as the Dirac–Hestenes equation. In this formulation all the components of the Dirac equation have an explicit geometric interpretation. Another related geometric equation is the Dirac–Kähler equation, which is a geometric analogue of the Dirac equation that can be defined on any general pseudo-Riemannian manifold and which acts on differential forms. In the case of a flat manifold, it reduces to four copies of the Dirac equation. However, on curved manifolds this decomposition breaks down and the equation fundamentally differs. This equation is used in lattice field theory to describe the continuum limit of staggered fermions.

### Weyl and Majorana equations

The Dirac spinor can be decomposed into a pair of Weyl spinors of opposite chirality $\psi ^{T}=(\psi _{L},\psi _{R})$ . Under Lorentz transformations, one transforms as a left-handed Weyl spinor $\psi _{L}$ and the other as a right-handed Weyl spinor $\psi _{R}$ . In the chiral representation of the gamma matrices, the Dirac equation reduces to the pair of equations for the Weyl spinors

$i\sigma ^{\mu }\partial _{\mu }\psi _{R}(x)=m\psi _{L}(x),$

$i{\bar {\sigma }}^{\mu }\partial _{\mu }\psi _{L}(x)=m\psi _{R}(x).$

In particular, in the massless limit the Weyl spinors decouple and the Dirac equation is equivalent to a pair of Weyl equations.

This decomposition has been proposed as an intuitive explanation of Zitterbewegung, as these massless components would propagate at the speed of light and move in opposite directions, since the helicity is the projection of the spin onto the direction of motion. Here the role of the mass is not to make the velocity less than the speed of light, but instead controls the average rate at which these reversals occur; specifically, the reversals can be modelled as a Poisson process.

A closely related equation is the Majorana equation, with this formally taking the same form as the Dirac equation except that it acts on Majorana spinors. These are spinors that satisfy a reality condition $\psi =C{\bar {\psi }}^{T}$ , where C is the charge-conjugation operator. In higher dimensions, the Dirac equation has similar relations to the equations describing other spinor representations that arise in those dimensions.

### Pauli equation

In the non-relativistic limit, the Dirac equation reduces to the Pauli equation, which when coupled to electromagnetism has the form

$\left[{\frac {1}{2m}}\left({\boldsymbol {\sigma }}\cdot ({\hat {\boldsymbol {p}}}-q{\boldsymbol {A}})\right)^{2}+q\phi \right]|\psi \rangle =0.$

Here ${\boldsymbol {\sigma }}$ is the vector of Pauli matrices and ${\hat {\boldsymbol {p}}}=-i\nabla$ is the momentum operator. The equation describes a fermion of charge q coupled to the electromagnetic field through a magnetic vector potential ${\boldsymbol {A}}$ and an electric scalar potential $\phi$ . The fermion is described through the two-component wave function $|\psi \rangle$ , where each component describes one of the two spin states $|\psi \rangle =\psi _{+}|\uparrow \rangle +\psi _{-}|\downarrow \rangle$ .

The Pauli equation is often used in quantum mechanics to describe phenomena where relativistic effects are negligible but the spin of the fermion is important. It can also be recast in a form which directly shows that the gyromagnetic ratio of the fermion described by the Dirac equation is exactly $g=2$ . In quantum electrodynamics there are additional quantum corrections that modify this value, give rise to a non-zero anomalous magnetic moment.

## Gauge symmetry

### Vector symmetry

The vector and axial symmetries of the Dirac action are both global symmetries, in that they act the same everywhere in spacetime. In classical field theory, the Lagrangian can always be modified in a way to elevate a global symmetry to a local symmetry, which can act differently at different spacetime locations. In the case of the vector symmetry, which corresponding to a global change of the spinor field by a phase $\psi \rightarrow e^{i\alpha }\psi$ , gauging would result in an action invariant under a local symmetry where the phase can take different values at different points $\psi \rightarrow e^{i\alpha (x)}\psi$ . While symmetries can always be gauged in classical field theory, this may not always be possible in the full quantum theory due to various obstructions such as anomalies, which signal that the full quantum theory is not invariant under the local symmetry despite its classical Lagrangian being invariant. For example, the axial symmetry in the massless Dirac theory with one fermion is anomalous due to the chiral anomaly and cannot be gauged.

Elevating the vector symmetry to a local symmetry means that the original action is no longer invariant under the symmetry due to the appearance of a $\partial _{\mu }\alpha (x)$ term arising from the kinetic term. Instead, a new field $A_{\mu }(x)$ , known as a gauge field, must be introduced. It must also transform under the local symmetry as

$A_{\mu }\rightarrow A_{\mu }+{\tfrac {1}{e}}\partial _{\mu }\alpha ,$

where e plays the role of the charge of the Dirac spinor to the gauge field. The Dirac action can then be made invariant under the local symmetry by replacing the derivative term with a new gauge covariant derivative

$D_{\mu }\psi =\partial _{\mu }\psi +ieA_{\mu }\psi .$

The Dirac action then takes the form

$S=\int d^{4}x{\bar {\psi }}(i{{D}\!\!\!\!/}-m)\psi =\int d^{4}x\left[{\bar {\psi }}(i{{\partial }\!\!\!/}-m)\psi -ej^{\mu }A_{\mu }\right].$

This result can also be directly acquired through the Noether procedure, which is the general principle that a global symmetry can be gauged through the introduction of a term coupling the gauge field to the appropriate global symmetry current. Additionally introducing the kinetic term for the gauge field results in the action for quantum electrodynamics.

### General symmetries

The symmetries that can be gauged can be greatly expanded by considering a theory with N identical Dirac spinors $\psi ^{a}$ labelled by a new index a . Together these spinors can be considered as being part of a single object $\psi$ with components $\psi ^{i,a}$ where i labels the four spin components, and a the different spinors. The largest global symmetry of this action is then given by the unitary group ${\text{U}}(N)$ .

Any continuous subgroup of ${\text{U}}(N)$ can then be gauged. In particular, if one wishes to gauge the symmetry acting on all N components, then the symmetry being gauged must admit an N -dimensional unitary representation acting on the spinors. That is, for every $g\in {\text{G}}\subseteq {\text{U}}(N)$ , there exists an $N\times N$ dimensional matrix representation $\rho (g)$ such that

$\psi (x)\rightarrow \rho (g)\psi (x)$

forms a faithful representation of the group. Gauging the largest continuous subgroup, ${\text{SU}}(N)$ , requires the spinors to transform in the fundamental or antifundamental representation. Gauging elevates the representation from being spacetime independent to being spacetime dependent $\rho (g(x))$ . It requires introducing a gauge field $A_{\mu }^{a}$ , formally the connection on the principal bundle, which necessarily transforms in the adjoint representation of the gauge group. The covariant derivative then takes the form

$D_{\mu }\psi =\partial _{\mu }\psi +{\tilde {\rho }}(A_{\mu })\psi .$

One symmetry that frequently gets gauged is the special unitary group ${\text{SU}}(N)$ symmetry. Spinors transforming in the fundamental representation transform as

$\psi (x)\rightarrow U(x)\psi (x),$

where $U(x)$ is a $N\times N$ unitary matrix corresponding to a particular group element. The gauge field is a matrix valued gauge field $A_{\mu }^{a}$ which transforms in the adjoint representation as

$A_{\mu }(x)\rightarrow U(x)A_{\mu }(x)U^{-1}(x)+{\frac {1}{g}}(\partial _{\mu }U(x))U^{-1}(x).$

The covariant derivative then takes the form

$D_{\mu }\psi =\partial _{\mu }\psi +igA_{\mu }\psi .$

By also introducing the kinetic term for the gauge field, one constructs the action for quantum chromodynamics

$S_{\text{QCD}}=\int d^{4}x\left[-{\tfrac {1}{4}}{\text{Tr}}(F^{\mu \nu }F_{\mu \nu })+{\bar {\psi }}(i{{D}\!\!\!/}-m)\psi \right],$

where in the gauge field kinetic term, the Yang–Mills fields strength tensor is defined as

$F_{\mu \nu }=\partial _{\mu }A_{\nu }-\partial _{\nu }A_{\mu }-ig[A_{\mu },A_{\nu }].$

The case of ${\text{SU}}(3)$ describes strong interactions of the quark sector of the Standard Model, with the gauge field corresponding to gluons and the Dirac spinors to the quarks. The ${\text{SU}}(2)$ case also plays a role in the Standard Model, describing the electroweak sector. The gauge field in this case is the W-boson, while the Dirac spinors are leptons.
