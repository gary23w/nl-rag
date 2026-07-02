---
title: "Angular momentum (part 2/2)"
source: https://en.wikipedia.org/wiki/Angular_momentum
domain: classical-mechanics
license: CC-BY-SA-4.0
tags: classical mechanics, newtonian mechanics, conservation of energy, angular momentum
fetched: 2026-07-02
part: 2/2
---

## Angular momentum in quantum mechanics

In quantum mechanics, angular momentum (like other quantities) is expressed as an operator, and its one-dimensional projections have quantized eigenvalues. Angular momentum is subject to the Heisenberg uncertainty principle, implying that at any time, only one projection (also called "component") can be measured with definite precision; the other two then remain uncertain. Because of this, the axis of rotation of a quantum particle is undefined. Quantum particles *do* possess a type of non-orbital angular momentum called "spin", but this angular momentum does not correspond to a spinning motion. In relativistic quantum mechanics the above relativistic definition becomes a tensorial operator.

### Spin, orbital, and total angular momentum

The classical definition of angular momentum as $\mathbf {L} =\mathbf {r} \times \mathbf {p}$ can be carried over to quantum mechanics, by reinterpreting **r** as the quantum position operator and **p** as the quantum momentum operator. **L** is then an operator, specifically called the *orbital angular momentum operator*. The components of the angular momentum operator satisfy the commutation relations of the Lie algebra SO(3). Indeed, these operators are precisely the infinitesimal action of the rotation group on the quantum Hilbert space. (See also the discussion below of the angular momentum operators as the generators of rotations.)

However, in quantum physics, there is another type of angular momentum, called *spin angular momentum*, represented by the spin operator **S**. Spin is often depicted as a particle literally spinning around an axis, but this is a misleading and inaccurate picture: spin is an intrinsic property of a particle, unrelated to any sort of motion in space and fundamentally different from orbital angular momentum. All elementary particles have a characteristic spin, which is nonzero for all elementary particles other than the Higgs boson (which has spin 0, making it the only known elementary scalar boson). For example, electrons have "spin 1/2" (this actually means "spin ħ/2"), photons have "spin 1" (this actually means "spin ħ"), and pi-mesons have spin 0.

Finally, there is total angular momentum **J**, which combines both the spin and orbital angular momentum of all particles and fields. (For one particle, **J** = **L** + **S**.) Conservation of angular momentum applies to **J**, but not to **L** or **S**; for example, the spin–orbit interaction allows angular momentum to transfer back and forth between **L** and **S**, with the total remaining constant. Electrons and photons need not have integer-based values for total angular momentum, but can also have half-integer values.

In molecules the total angular momentum **F** is the sum of the rovibronic (orbital) angular momentum **N**, the electron spin angular momentum **S**, and the nuclear spin angular momentum **I**. For electronic singlet states the rovibronic angular momentum is denoted **J** rather than **N**. As explained by Van Vleck, the components of the molecular rovibronic angular momentum referred to molecule-fixed axes have different commutation relations from those for the components about space-fixed axes.

### Quantization

In quantum mechanics, angular momentum is quantized – that is, it cannot vary continuously, but only in "quantum leaps" between certain allowed values. For any system, the following restrictions on measurement results apply, where $\hbar$ is the reduced Planck constant and ${\hat {n}}$ is any Euclidean vector such as x, y, or z:

| **If you measure...** | **The result can be...** |
|---|---|
| $L_{\hat {n}}$ | $\ldots ,-2\hbar ,-\hbar ,0,\hbar ,2\hbar ,\ldots$ |
| $S_{\hat {n}}$ or $J_{\hat {n}}$ | $\ldots ,-{\frac {3}{2}}\hbar ,-\hbar ,-{\frac {1}{2}}\hbar ,0,{\frac {1}{2}}\hbar ,\hbar ,{\frac {3}{2}}\hbar ,\ldots$ |
| ${\begin{aligned}&L^{2}\\={}&L_{x}^{2}+L_{y}^{2}+L_{z}^{2}\end{aligned}}$ | $\left[\hbar ^{2}n(n+1)\right]$ , where $n=0,1,2,\ldots$ |
| $S^{2}$ or $J^{2}$ | $\left[\hbar ^{2}n(n+1)\right]$ , where $n=0,{\tfrac {1}{2}},1,{\tfrac {3}{2}},\ldots$ |

The reduced Planck constant $\hbar$ is tiny by everyday standards, about 10−34 J s, and therefore this quantization does not noticeably affect the angular momentum of macroscopic objects. However, it is very important in the microscopic world. For example, the structure of electron shells and subshells in chemistry is significantly affected by the quantization of angular momentum.

Quantization of angular momentum was first postulated by Niels Bohr in his model of the atom and was later predicted by Erwin Schrödinger in his Schrödinger equation.

### Uncertainty

In the definition $\mathbf {L} =\mathbf {r} \times \mathbf {p}$ , six operators are involved: The position operators $r_{x}$ , $r_{y}$ , $r_{z}$ , and the momentum operators $p_{x}$ , $p_{y}$ , $p_{z}$ . However, the Heisenberg uncertainty principle tells us that it is not possible for all six of these quantities to be known simultaneously with arbitrary precision. Therefore, there are limits to what can be known or measured about a particle's angular momentum. It turns out that the best that one can do is to simultaneously measure both the angular momentum vector's magnitude and its component along one axis.

The uncertainty is closely related to the fact that different components of an angular momentum operator do not commute, for example $L_{x}L_{y}\neq L_{y}L_{x}$ . (For the precise commutation relations, see angular momentum operator.)

### Total angular momentum as generator of rotations

As mentioned above, orbital angular momentum **L** is defined as in classical mechanics: $\mathbf {L} =\mathbf {r} \times \mathbf {p}$ , but *total* angular momentum **J** is defined in a different, more basic way: **J** is defined as the "generator of rotations". More specifically, **J** is defined so that the operator $R({\hat {n}},\phi )\equiv \exp \left(-{\frac {i}{\hbar }}\phi \,\mathbf {J} \cdot {\hat {\mathbf {n} }}\right)$ is the rotation operator that takes any system and rotates it by angle $\phi$ about the axis ${\hat {\mathbf {n} }}$ . (The "exp" in the formula refers to operator exponential.) To put this the other way around, whatever our quantum Hilbert space is, we expect that the rotation group SO(3) will act on it. There is then an associated action of the Lie algebra so(3) of SO(3); the operators describing the action of so(3) on our Hilbert space are the (total) angular momentum operators.

The relationship between the angular momentum operator and the rotation operators is the same as the relationship between Lie algebras and Lie groups in mathematics. The close relationship between angular momentum and rotations is reflected in Noether's theorem that proves that angular momentum is conserved whenever the laws of physics are rotationally invariant.


## Angular momentum in electrodynamics

When describing the motion of a charged particle in an electromagnetic field, the canonical momentum **P** (derived from the Lagrangian for this system) is not gauge invariant. As a consequence, the canonical angular momentum **L** = **r** × **P** is not gauge invariant either. Instead, the momentum that is physical, the so-called *kinetic momentum* (used throughout this article), is (in SI units) $\mathbf {p} =m\mathbf {v} =\mathbf {P} -e\mathbf {A}$ where *e* is the electric charge of the particle and **A** the magnetic vector potential of the electromagnetic field. The gauge-invariant angular momentum, that is *kinetic angular momentum*, is given by $\mathbf {K} =\mathbf {r} \times (\mathbf {P} -e\mathbf {A} )$

The interplay with quantum mechanics is discussed further in the article on canonical commutation relations.


## Angular momentum in optics

In *classical Maxwell electrodynamics* the Poynting vector is a linear momentum density of electromagnetic field. $\mathbf {S} (\mathbf {r} ,t)=\epsilon _{0}c^{2}\mathbf {E} (\mathbf {r} ,t)\times \mathbf {B} (\mathbf {r} ,t).$

The angular momentum density vector $\mathbf {L} (\mathbf {r} ,t)$ is given by a vector product as in classical mechanics: $\mathbf {L} (\mathbf {r} ,t)=\epsilon _{0}\mu _{0}\mathbf {r} \times \mathbf {S} (\mathbf {r} ,t).$

The above identities are valid *locally*, i.e. in each space point $\mathbf {r}$ in a given moment t .


## Angular momentum in nature and the cosmos

Tropical cyclones and other related weather phenomena involve conservation of angular momentum in order to explain the dynamics. Winds revolve slowly around low pressure systems, mainly due to the coriolis effect. If the low pressure intensifies and the slowly circulating air is drawn toward the center, the molecules must speed up in order to conserve angular momentum. By the time they reach the center, the speeds become destructive.

Johannes Kepler determined the laws of planetary motion without knowledge of conservation of momentum. However, not long after his discovery their derivation was determined from conservation of angular momentum. Planets move more slowly the further they are out in their elliptical orbits, which is explained intuitively by the fact that orbital angular momentum is proportional to the radius of the orbit. Since the mass does not change and the angular momentum is conserved, the velocity drops.

Tidal acceleration is an effect of the tidal forces between an orbiting natural satellite (e.g. the Moon) and the primary planet that it orbits (e.g. Earth). The gravitational torque between the Moon and the tidal bulge of Earth causes the Moon to be constantly promoted to a slightly higher orbit (~3.8 cm per year) and Earth to be decelerated (by −25.858 ± 0.003″/cy²) in its rotation (the length of the day increases by ~1.7 ms per century, +2.3 ms from tidal effect and −0.6 ms from post-glacial rebound). The Earth loses angular momentum which is transferred to the Moon such that the overall angular momentum is conserved.


## Angular momentum in engineering and technology

Examples of using conservation of angular momentum for practical advantage are abundant. In engines such as steam engines or internal combustion engines, a flywheel is needed to efficiently convert the lateral motion of the pistons to rotational motion.

Inertial navigation systems explicitly use the fact that angular momentum is conserved with respect to the inertial frame of space. Inertial navigation is what enables submarine trips under the polar ice cap, but are also crucial to all forms of modern navigation.

Rifled bullets use the stability provided by conservation of angular momentum to be more true in their trajectory. The invention of rifled firearms and cannons gave their users significant strategic advantage in battle, and thus were a technological turning point in history.


## History

Isaac Newton, in the *Principia*, hinted at angular momentum in his examples of the first law of motion,

> A top, whose parts by their cohesion are perpetually drawn aside from rectilinear motions, does not cease its rotation, otherwise than as it is retarded by the air. The greater bodies of the planets and comets, meeting with less resistance in more free spaces, preserve their motions both progressive and circular for a much longer time.

He did not further investigate angular momentum directly in the *Principia*, saying:

> From such kind of reflexions also sometimes arise the circular motions of bodies about their own centers. But these are cases which I do not consider in what follows; and it would be too tedious to demonstrate every particular that relates to this subject.

However, his geometric proof of the law of areas is an outstanding example of Newton's genius, and indirectly proves angular momentum conservation in the case of a central force.

### Law of Areas

#### Newton's derivation

As a planet orbits the Sun, the line between the Sun and the planet sweeps out equal areas in equal intervals of time. This had been known since Kepler expounded his second law of planetary motion. Newton derived a unique geometric proof, and went on to show that the attractive force of the Sun's gravity was the cause of all of Kepler's laws.

During the first interval of time, an object is in motion from point **A** to point **B**. Undisturbed, it would continue to point **c** during the second interval. When the object arrives at **B**, it receives an impulse directed toward point **S**. The impulse gives it a small added velocity toward **S**, such that if this were its only velocity, it would move from **B** to **V** during the second interval. By the rules of velocity composition, these two velocities add, and point **C** is found by construction of parallelogram **BcCV**. Thus the object's path is deflected by the impulse so that it arrives at point **C** at the end of the second interval. Because the triangles **SBc** and **SBC** have the same base **SB** and the same height **Bc** or **VC**, they have the same area. By symmetry, triangle **SBc** also has the same area as triangle **SAB**, therefore the object has swept out equal areas **SAB** and **SBC** in equal times.

At point **C**, the object receives another impulse toward **S**, again deflecting its path during the third interval from **d** to **D**. Thus it continues to **E** and beyond, the triangles **SAB**, **SBc**, **SBC**, **SCd**, **SCD**, **SDe**, **SDE** all having the same area. Allowing the time intervals to become ever smaller, the path **ABCDE** approaches indefinitely close to a continuous curve.

Note that because this derivation is geometric, and no specific force is applied, it proves a more general law than Kepler's second law of planetary motion. It shows that the Law of Areas applies to any central force, attractive or repulsive, continuous or non-continuous, or zero.

#### Conservation of angular momentum in the law of areas

The proportionality of angular momentum to the area swept out by a moving object can be understood by realizing that the bases of the triangles, that is, the lines from **S** to the object, are equivalent to the radius *r*, and that the heights of the triangles are proportional to the perpendicular component of velocity *v*⊥. Hence, if the area swept per unit time is constant, then by the triangular area formula ⁠1/2⁠(base)(height), the product (base)(height) and therefore the product *rv*⊥ are constant: if *r* and the base length are decreased, *v*⊥ and height must increase proportionally. Mass is constant, therefore angular momentum *rmv*⊥ is conserved by this exchange of distance and velocity.

In the case of triangle **SBC**, area is equal to ⁠1/2⁠(**SB**)(**VC**). Wherever **C** is eventually located due to the impulse applied at **B**, the product (**SB**)(**VC**), and therefore *rmv*⊥ remain constant. Similarly so for each of the triangles.

Another areal proof of conservation of angular momentum for any central force uses Mamikon's sweeping tangents theorem.

### After Newton

Leonhard Euler, Daniel Bernoulli, and Patrick d'Arcy all understood angular momentum in terms of conservation of areal velocity, a result of their analysis of Kepler's second law of planetary motion. It is unlikely that they realized the implications for ordinary rotating matter.

In 1736 Euler, like Newton, touched on some of the equations of angular momentum in his *Mechanica* without further developing them.

Bernoulli wrote in a 1744 letter of a "moment of rotational motion", possibly the first conception of angular momentum as we now understand it.

In 1799, Pierre-Simon Laplace first realized that a fixed plane was associated with rotation—his *invariable plane*.

Louis Poinsot in 1803 began representing rotations as a line segment perpendicular to the rotation, and elaborated on the "conservation of moments".

In 1852 Léon Foucault used a gyroscope in an experiment to display the Earth's rotation.

William J. M. Rankine's 1858 *Manual of Applied Mechanics* defined angular momentum in the modern sense for the first time:

> ... a line whose length is proportional to the magnitude of the angular momentum, and whose direction is perpendicular to the plane of motion of the body and of the fixed point, and such, that when the motion of the body is viewed from the extremity of the line, the radius-vector of the body seems to have right-handed rotation.

In an 1872 edition of the same book, Rankine stated that "The term *angular momentum* was introduced by Mr. Hayward," probably referring to R.B. Hayward's article *On a Direct Method of estimating Velocities, Accelerations, and all similar Quantities with respect to Axes moveable in any manner in Space with Applications,* which was introduced in 1856, and published in 1864. Rankine was mistaken, as numerous publications feature the term starting in the late 18th to early 19th centuries. However, Hayward's article apparently was the first use of the term and the concept seen by much of the English-speaking world. Before this, angular momentum was typically referred to as "momentum of rotation" in English.
