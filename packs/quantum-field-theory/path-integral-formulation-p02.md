---
title: "Path-integral formulation (part 2/2)"
source: https://en.wikipedia.org/wiki/Path_integral_formulation
domain: quantum-field-theory
license: CC-BY-SA-4.0
tags: quantum field theory, gauge theory, feynman diagram, path integral formulation
fetched: 2026-07-02
part: 2/2
---

## Quantum field theory

Both the Schrödinger and Heisenberg approaches to quantum mechanics single out time and are not in the spirit of relativity. For example, the Heisenberg approach requires that scalar field operators obey the commutation relation

$[\varphi (x),\partial _{t}\varphi (y)]=i\delta ^{3}(x-y)$

for two simultaneous spatial positions x and y, and this is not a relativistically invariant concept. The results of a calculation *are* covariant, but the symmetry is not apparent in intermediate stages. If naive field-theory calculations did not produce infinite answers in the continuum limit, this would not have been such a big problem – it would just have been a bad choice of coordinates. But the lack of symmetry means that the infinite quantities must be cut off, and the bad coordinates make it nearly impossible to cut off the theory without spoiling the symmetry. This makes it difficult to extract the physical predictions, which require a careful limiting procedure.

The problem of lost symmetry also appears in classical mechanics, where the Hamiltonian formulation also superficially singles out time. The Lagrangian formulation makes the relativistic invariance apparent. In the same way, the path integral is manifestly relativistic. It reproduces the Schrödinger equation, the Heisenberg equations of motion, and the canonical commutation relations and shows that they are compatible with relativity. It extends the Heisenberg-type operator algebra to operator product rules, which are new relations difficult to see in the old formalism.

Further, different choices of canonical variables lead to very different-seeming formulations of the same theory. The transformations between the variables can be very complicated, but the path integral makes them into reasonably straightforward changes of integration variables. For these reasons, the Feynman path integral has made earlier formalisms largely obsolete.

The price of a path integral representation is that the unitarity of a theory is no longer self-evident, but it can be proven by changing variables to some canonical representation. The path integral itself also deals with larger mathematical spaces than is usual, which requires more careful mathematics, not all of which has been fully worked out. The path integral historically was not immediately accepted, partly because it took many years to incorporate fermions properly. This required physicists to invent an entirely new mathematical object – the Grassmann variable – which also allowed changes of variables to be done naturally, as well as allowing constrained quantization.

The integration variables in the path integral are subtly non-commuting. The value of the product of two field operators at what looks like the same point depends on how the two points are ordered in space and time. This makes some naive identities fail.

### Propagator

In relativistic theories, there is both a particle and field representation for every theory. The field representation is a sum over all field configurations, and the particle representation is a sum over different particle paths.

The nonrelativistic formulation is traditionally given in terms of particle paths, not fields. There, the path integral in the usual variables, with fixed boundary conditions, gives the probability amplitude for a particle to go from point x to point y in time T:

$K(x,y;T)=\langle y;T\mid x;0\rangle =\int _{x(0)=x}^{x(T)=y}e^{iS[x]}\,Dx.$

This is called the propagator. To obtain the final state at *y*, apply *K*(*x*,*y*; *T*) to the initial state and integrate over *x* resulting in:

$\psi _{T}(y)=\int _{x}\psi _{0}(x)K(x,y;T)\,dx=\int ^{x(T)=y}\psi _{0}(x(0))e^{iS[x]}\,Dx.$

For a spatially homogeneous system, where *K*(*x*, *y*) is only a function of (*x* − *y*), the integral is a convolution, the final state is the initial state convolved with the propagator:

$\psi _{T}=\psi _{0}*K(;T).$

For a free particle of mass m, the propagator can be evaluated either explicitly from the path integral or by noting that the Schrödinger equation is a diffusion equation in imaginary time, and the solution must be a normalized Gaussian:

$K(x,y;T)\propto e^{\frac {im(x-y)^{2}}{2T}}.$

Taking the Fourier transform in (*x* − *y*) produces another Gaussian:

$K(p;T)=e^{\frac {iTp^{2}}{2m}},$

and in p-space the proportionality factor here is constant in time, as will be verified in a moment. The Fourier transform in time, extending *K*(*p*; *T*) to be zero for negative times, gives Green's function, or the frequency-space propagator:

$G_{\text{F}}(p,E)={\frac {-i}{E-{\frac {{\vec {p}}^{2}}{2m}}+i\varepsilon }},$

which is the reciprocal of the operator that annihilates the wavefunction in the Schrödinger equation, which wouldn't have come out right if the proportionality factor weren't constant in the p-space representation.

The infinitesimal term in the denominator is a small positive number, which guarantees that the inverse Fourier transform in E will be nonzero only for future times. For past times, the inverse Fourier transform contour closes toward values of E where there is no singularity. This guarantees that K propagates the particle into the future and is the reason for the subscript "F" on G. The infinitesimal term can be interpreted as an infinitesimal rotation toward imaginary time.

It is also possible to reexpress the nonrelativistic time evolution in terms of propagators going toward the past, since the Schrödinger equation is time-reversible. The past propagator is the same as the future propagator except for the obvious difference that it vanishes in the future, and in the Gaussian t is replaced by −*t*. In this case, the interpretation is that these are the quantities to convolve the final wavefunction so as to get the initial wavefunction:

$G_{\text{B}}(p,E)={\frac {-i}{-E-{\frac {i{\vec {p}}^{2}}{2m}}+i\varepsilon }}.$

Given the nearly identical only change is the sign of E and ε, the parameter E in Green's function can either be the energy if the paths are going toward the future, or the negative of the energy if the paths are going toward the past.

For a nonrelativistic theory, the time as measured along the path of a moving particle and the time as measured by an outside observer are the same. In relativity, this is no longer true. For a relativistic theory the propagator should be defined as the sum over all paths that travel between two points in a fixed proper time, as measured along the path (these paths describe the trajectory of a particle in space and in time):

$K(x-y,\mathrm {T} )=\int _{x(0)=x}^{x(\mathrm {T} )=y}e^{i\int _{0}^{\mathrm {T} }{\sqrt {{\dot {x}}^{2}-\alpha }}\,d\tau }.$

The integral above is not trivial to interpret because of the square root. Fortunately, there is a heuristic trick. The sum is over the relativistic arc length of the path of an oscillating quantity, and like the nonrelativistic path integral should be interpreted as slightly rotated into imaginary time. The function *K*(*x* − *y*, *τ*) can be evaluated when the sum is over paths in Euclidean space:

$K(x-y,\mathrm {T} )=e^{-\alpha \mathrm {T} }\int _{x(0)=x}^{x(\mathrm {T} )=y}e^{-L}.$

This describes a sum over all paths of length Τ of the exponential of minus the length. This can be given a probability interpretation. The sum over all paths is a probability average over a path constructed step by step. The total number of steps is proportional to Τ, and each step is less likely the longer it is. By the central limit theorem, the result of many independent steps is a Gaussian of variance proportional to Τ:

$K(x-y,\mathrm {T} )=e^{-\alpha \mathrm {T} }e^{-{\frac {(x-y)^{2}}{\mathrm {T} }}}.$

The usual definition of the relativistic propagator only asks for the amplitude to travel from x to y, after summing over all the possible proper times it could take:

$K(x-y)=\int _{0}^{\infty }K(x-y,\mathrm {T} )W(\mathrm {T} )\,d\mathrm {T} ,$

where *W*(Τ) is a weight factor, the relative importance of paths of different proper time. By the translation symmetry in proper time, this weight can only be an exponential factor and can be absorbed into the constant α:

$K(x-y)=\int _{0}^{\infty }e^{-{\frac {(x-y)^{2}}{\mathrm {T} }}-\alpha \mathrm {T} }\,d\mathrm {T} .$

This is the Schwinger representation. Taking a Fourier transform over the variable (*x* − *y*) can be done for each value of Τ separately, and because each separate Τ contribution is a Gaussian, gives whose Fourier transform is another Gaussian with reciprocal width. So in p-space, the propagator can be reexpressed simply:

$K(p)=\int _{0}^{\infty }e^{-\mathrm {T} p^{2}-\mathrm {T} \alpha }\,d\mathrm {T} ={\frac {1}{p^{2}+\alpha }},$

which is the Euclidean propagator for a scalar particle. Rotating *p*0 to be imaginary gives the usual relativistic propagator, up to a factor of −*i* and an ambiguity, which will be clarified below:

$K(p)={\frac {i}{p_{0}^{2}-{\vec {p}}^{2}-m^{2}}}.$

This expression can be interpreted in the nonrelativistic limit, where it is convenient to split it by partial fractions:

$2p_{0}K(p)={\frac {i}{p_{0}-{\sqrt {{\vec {p}}^{2}+m^{2}}}}}+{\frac {i}{p_{0}+{\sqrt {{\vec {p}}^{2}+m^{2}}}}}.$

For states where one nonrelativistic particle is present, the initial wavefunction has a frequency distribution concentrated near *p*0 = *m*. When convolving with the propagator, which in p space just means multiplying by the propagator, the second term is suppressed and the first term is enhanced. For frequencies near *p*0 = *m*, the dominant first term has the form

$2mK_{\text{NR}}(p)={\frac {i}{(p_{0}-m)-{\frac {{\vec {p}}^{2}}{2m}}}}.$

This is the expression for the nonrelativistic Green's function of a free Schrödinger particle.

The second term has a nonrelativistic limit also, but this limit is concentrated on frequencies that are negative. The second pole is dominated by contributions from paths where the proper time and the coordinate time are ticking in an opposite sense, which means that the second term is to be interpreted as the antiparticle. The nonrelativistic analysis shows that with this form the antiparticle still has positive energy.

The proper way to express this mathematically is that, adding a small suppression factor in proper time, the limit where *t* → −∞ of the first term must vanish, while the *t* → +∞ limit of the second term must vanish. In the Fourier transform, this means shifting the pole in *p*0 slightly, so that the inverse Fourier transform will pick up a small decay factor in one of the time directions:

$K(p)={\frac {i}{p_{0}-{\sqrt {{\vec {p}}^{2}+m^{2}}}+i\varepsilon }}+{\frac {i}{p_{0}-{\sqrt {{\vec {p}}^{2}+m^{2}}}-i\varepsilon }}.$

Without these terms, the pole contribution could not be unambiguously evaluated when taking the inverse Fourier transform of *p*0. The terms can be recombined:

$K(p)={\frac {i}{p^{2}-m^{2}+i\varepsilon }},$

which when factored, produces opposite-sign infinitesimal terms in each factor. This is the mathematically precise form of the relativistic particle propagator, free of any ambiguities. The ε term introduces a small imaginary part to the *α* = *m*2, which in the Minkowski version is a small exponential suppression of long paths.

So in the relativistic case, the Feynman path-integral representation of the propagator includes paths going backwards in time, which describe antiparticles. The paths that contribute to the relativistic propagator go forward and backwards in time, and the interpretation of this is that the amplitude for a free particle to travel between two points includes amplitudes for the particle to fluctuate into an antiparticle, travel back in time, then forward again.

Unlike the nonrelativistic case, it is impossible to produce a relativistic theory of local particle propagation without including antiparticles. All local differential operators have inverses that are nonzero outside the light cone, meaning that it is impossible to keep a particle from travelling faster than light. Such a particle cannot have a Green's function that is only nonzero in the future in a relativistically invariant theory.

### Functionals of fields

However, the path integral formulation is also extremely important in *direct* application to quantum field theory, in which the "paths" or histories being considered are not the motions of a single particle, but the possible time evolutions of a field over all space. The action is referred to technically as a functional of the field: *S*[*ϕ*], where the field *ϕ*(*xμ*) is itself a function of space and time, and the square brackets are a reminder that the action depends on all the field's values everywhere, not just some particular value. *One* such given function *ϕ*(*xμ*) of spacetime is called a *field configuration*. In principle, one integrates Feynman's amplitude over the class of all possible field configurations.

Much of the formal study of QFT is devoted to the properties of the resulting functional integral, and much effort (not yet entirely successful) has been made toward making these functional integrals mathematically precise.

Such a functional integral is extremely similar to the partition function in statistical mechanics. Indeed, it is sometimes *called* a partition function, and the two are essentially mathematically identical except for the factor of i in the exponent in Feynman's postulate 3. Analytically continuing the integral to an imaginary time variable (called a Wick rotation) makes the functional integral even more like a statistical partition function and also tames some of the mathematical difficulties of working with these integrals.

### Expectation values

In quantum field theory, if the action is given by the functional S of field configurations (which only depends locally on the fields), then the time-ordered vacuum expectation value of polynomially bounded functional F, ⟨*F*⟩, is given by

$\langle F\rangle ={\frac {\int {\mathcal {D}}\varphi F[\varphi ]e^{i{\mathcal {S}}[\varphi ]}}{\int {\mathcal {D}}\varphi e^{i{\mathcal {S}}[\varphi ]}}}.$

The symbol ∫D*ϕ* here is a concise way to represent the infinite-dimensional integral over all possible field configurations on all of space-time. As stated above, the unadorned path integral in the denominator ensures proper normalization.

### As a probability

Strictly speaking, the only question that can be asked in physics is: *What fraction of states satisfying condition A also satisfy condition B?* The answer to this is a number between 0 and 1, which can be interpreted as a conditional probability, written as P(*B*|*A*). In terms of path integration, since P(*B*|*A*) = ⁠P(*A*∩*B*) / P(*A*)⁠, this means

$\operatorname {P} (B\mid A)={\frac {\sum _{F\subset A\cap B}\left|\int {\mathcal {D}}\varphi O_{\text{in}}[\varphi ]e^{i{\mathcal {S}}[\varphi ]}F[\varphi ]\right|^{2}}{\sum _{F\subset A}\left|\int {\mathcal {D}}\varphi O_{\text{in}}[\varphi ]e^{i{\mathcal {S}}[\varphi ]}F[\varphi ]\right|^{2}}},$

where the functional *O*in[*ϕ*] is the superposition of all incoming states that could lead to the states we are interested in. In particular, this could be a state corresponding to the state of the Universe just after the Big Bang, although for actual calculation this can be simplified using heuristic methods. Since this expression is a quotient of path integrals, it is naturally normalised.

### Schwinger–Dyson equations

Since this formulation of quantum mechanics is analogous to classical action principle, one might expect that identities concerning the action in classical mechanics would have quantum counterparts derivable from a functional integral. This is often the case.

In the language of functional analysis, we can write the Euler–Lagrange equations as

${\frac {\delta {\mathcal {S}}[\varphi ]}{\delta \varphi }}=0$

(the left-hand side is a functional derivative; the equation means that the action is stationary under small changes in the field configuration). The quantum analogues of these equations are called the Schwinger–Dyson equations.

If the functional measure D*ϕ* turns out to be translationally invariant (we'll assume this for the rest of this article, although this does not hold for, let's say nonlinear sigma models), and if we assume that after a Wick rotation

$e^{i{\mathcal {S}}[\varphi ]},$

which now becomes

$e^{-H[\varphi ]}$

for some H, it goes to zero faster than a reciprocal of any polynomial for large values of φ, then we can integrate by parts (after a Wick rotation, followed by a Wick rotation back) to get the following Schwinger–Dyson equations for the expectation:

$\left\langle {\frac {\delta F[\varphi ]}{\delta \varphi }}\right\rangle =-i\left\langle F[\varphi ]{\frac {\delta {\mathcal {S}}[\varphi ]}{\delta \varphi }}\right\rangle$

for any polynomially-bounded functional F. In the deWitt notation this looks like

$\left\langle F_{,i}\right\rangle =-i\left\langle F{\mathcal {S}}_{,i}\right\rangle .$

These equations are the analog of the on-shell EL equations. The time ordering is taken before the time derivatives inside the S,*i*.

If J (called the source field) is an element of the dual space of the field configurations (which has at least an affine structure because of the assumption of the translational invariance for the functional measure), then the generating functional Z of the source fields is **defined** to be

$Z[J]=\int {\mathcal {D}}\varphi e^{i\left({\mathcal {S}}[\varphi ]+\langle J,\varphi \rangle \right)}.$

Note that

${\frac {\delta ^{n}Z}{\delta J(x_{1})\cdots \delta J(x_{n})}}[J]=i^{n}\,Z[J]\,\left\langle \varphi (x_{1})\cdots \varphi (x_{n})\right\rangle _{J},$

or

$Z^{,i_{1}\cdots i_{n}}[J]=i^{n}Z[J]\left\langle \varphi ^{i_{1}}\cdots \varphi ^{i_{n}}\right\rangle _{J},$

where

$\langle F\rangle _{J}={\frac {\int {\mathcal {D}}\varphi F[\varphi ]e^{i\left({\mathcal {S}}[\varphi ]+\langle J,\varphi \rangle \right)}}{\int {\mathcal {D}}\varphi e^{i\left({\mathcal {S}}[\varphi ]+\langle J,\varphi \rangle \right)}}}.$

Basically, if D*φ* *e**i*S[*φ*] is viewed as a functional distribution (this shouldn't be taken too literally as an interpretation of QFT, unlike its Wick-rotated statistical mechanics analogue, because we have time ordering complications here!), then ⟨*φ*(*x*1) ... *φ*(*xn*)⟩ are its moments, and Z is its Fourier transform.

If F is a functional of φ, then for an operator K, *F*[*K*] is defined to be the operator that substitutes K for φ. For example, if

$F[\varphi ]={\frac {\partial ^{k_{1}}}{\partial x_{1}^{k_{1}}}}\varphi (x_{1})\cdots {\frac {\partial ^{k_{n}}}{\partial x_{n}^{k_{n}}}}\varphi (x_{n}),$

and G is a functional of J, then

$F\left[-i{\frac {\delta }{\delta J}}\right]G[J]=(-i)^{n}{\frac {\partial ^{k_{1}}}{\partial x_{1}^{k_{1}}}}{\frac {\delta }{\delta J(x_{1})}}\cdots {\frac {\partial ^{k_{n}}}{\partial x_{n}^{k_{n}}}}{\frac {\delta }{\delta J(x_{n})}}G[J].$

Then, from the properties of the functional integrals

$\left\langle {\frac {\delta {\mathcal {S}}}{\delta \varphi (x)}}[\varphi ]+J(x)\right\rangle _{J}=0$

we get the "master" Schwinger–Dyson equation:

${\frac {\delta {\mathcal {S}}}{\delta \varphi (x)}}\left[-i{\frac {\delta }{\delta J}}\right]Z[J]+J(x)Z[J]=0,$

or

${\mathcal {S}}_{,i}[-i\partial ]Z+J_{i}Z=0.$

If the functional measure is not translationally invariant, it might be possible to express it as the product *M*[*φ*] D*φ*, where M is a functional and D*φ* is a translationally invariant measure. This is true, for example, for nonlinear sigma models where the target space is diffeomorphic to **R***n*. However, if the target manifold is some topologically nontrivial space, the concept of a translation does not even make any sense.

In that case, we would have to replace the S in this equation by another functional

${\hat {\mathcal {S}}}={\mathcal {S}}-i\ln M.$

If we expand this equation as a Taylor series about *J* = 0, we get the entire set of Schwinger–Dyson equations.


## Localization

The path integrals are usually thought of as being the sum of all paths through an infinite space–time. However, in local quantum field theory we would restrict everything to lie within a finite *causally complete* region, for example inside a double light-cone. This gives a more mathematically precise and physically rigorous definition of quantum field theory.

### Ward–Takahashi identities

Now how about the on shell Noether's theorem for the classical case? Does it have a quantum analog as well? Yes, but with a caveat. The functional measure would have to be invariant under the one parameter group of symmetry transformation as well.

Let's just assume for simplicity here that the symmetry in question is local (not local in the sense of a gauge symmetry, but in the sense that the transformed value of the field at any given point under an infinitesimal transformation would only depend on the field configuration over an arbitrarily small neighborhood of the point in question). Let's also assume that the action is local in the sense that it is the integral over spacetime of a Lagrangian, and that

$Q[{\mathcal {L}}(x)]=\partial _{\mu }f^{\mu }(x)$

for some function f where f only depends locally on φ (and possibly the spacetime position).

If we don't assume any special boundary conditions, this would not be a "true" symmetry in the true sense of the term in general unless *f* = 0 or something. Here, Q is a derivation that generates the one parameter group in question. We could have antiderivations as well, such as BRST and supersymmetry.

Let's also assume

$\int {\mathcal {D}}\varphi \,Q[F][\varphi ]=0$

for any polynomially-bounded functional F. This property is called the invariance of the measure, and this does not hold in general. (See *anomaly (physics)* for more details.)

Then,

$\int {\mathcal {D}}\varphi \,Q\left[Fe^{iS}\right][\varphi ]=0,$

which implies

$\langle Q[F]\rangle +i\left\langle F\int _{\partial V}f^{\mu }\,ds_{\mu }\right\rangle =0$

where the integral is over the boundary. This is the quantum analog of Noether's theorem.

Now, let's assume even further that Q is a local integral

$Q=\int d^{d}x\,q(x)$

where

$q(x)[\varphi (y)]=\delta ^{(d)}(X-y)Q[\varphi (y)]\,$

so that\

$q(x)[S]=\partial _{\mu }j^{\mu }(x)\,$

where

$j^{\mu }(x)=f^{\mu }(x)-{\frac {\partial }{\partial (\partial _{\mu }\varphi )}}{\mathcal {L}}(x)Q[\varphi ]\,$

(this is assuming the Lagrangian only depends on φ and its first partial derivatives! More general Lagrangians would require a modification to this definition!). We're not insisting that *q*(*x*) is the generator of a symmetry (i.e. we are *not* insisting upon the gauge principle), but just that Q is. And we also assume the even stronger assumption that the functional measure is locally invariant:

$\int {\mathcal {D}}\varphi \,q(x)[F][\varphi ]=0.$

Then, we would have

$\langle q(x)[F]\rangle +i\langle Fq(x)[S]\rangle =\langle q(x)[F]\rangle +i\left\langle F\partial _{\mu }j^{\mu }(x)\right\rangle =0.$

Alternatively,

$q(x)[S]\left[-i{\frac {\delta }{\delta J}}\right]Z[J]+J(x)Q[\varphi (x)]\left[-i{\frac {\delta }{\delta J}}\right]Z[J]=\partial _{\mu }j^{\mu }(x)\left[-i{\frac {\delta }{\delta J}}\right]Z[J]+J(x)Q[\varphi (x)]\left[-i{\frac {\delta }{\delta J}}\right]Z[J]=0.$

The above two equations are the Ward–Takahashi identities.

Now for the case where *f* = 0, we can forget about all the boundary conditions and locality assumptions. We'd simply have

$\left\langle Q[F]\right\rangle =0.$

Alternatively,

$\int d^{d}x\,J(x)Q[\varphi (x)]\left[-i{\frac {\delta }{\delta J}}\right]Z[J]=0.$


## Caveats

### Need for regulators and renormalization

Path integrals as they are defined here require the introduction of regulators. Changing the scale of the regulator leads to the renormalization group. In fact, renormalization is the major obstruction to making path integrals well-defined.

### Ordering prescription

Regardless of whether one works in configuration space or phase space, when equating the operator formalism and the path integral formulation, an ordering prescription is required to resolve the ambiguity in the correspondence between non-commutative operators and the commutative functions that appear in path integrands. For example, the operator ${\frac {1}{2}}({\hat {q}}{\hat {p}}+{\hat {p}}{\hat {q}})$ can be translated back as either $qp-{\frac {i\hbar }{2}}$ , $qp+{\frac {i\hbar }{2}}$ , or $qp$ depending on whether one chooses the ${\hat {q}}{\hat {p}}$ , ${\hat {p}}{\hat {q}}$ , or Weyl ordering prescription; conversely, $qp$ can be translated to either ${\hat {q}}{\hat {p}}$ , ${\hat {p}}{\hat {q}}$ , or ${\frac {1}{2}}({\hat {q}}{\hat {p}}+{\hat {p}}{\hat {q}})$ for the same respective choice of ordering prescription.


## Path integral in quantum-mechanical interpretation

In one interpretation of quantum mechanics, the "sum over histories" interpretation, the path integral is taken to be fundamental, and reality is viewed as a single indistinguishable "class" of paths that all share the same events. For this interpretation, it is crucial to understand what exactly an event is. The sum-over-histories method gives identical results to canonical quantum mechanics, and Sinha and Sorkin claim the interpretation explains the Einstein–Podolsky–Rosen paradox without resorting to nonlocality.

Some advocates of interpretations of quantum mechanics emphasizing decoherence have attempted to make more rigorous the notion of extracting a classical-like "coarse-grained" history from the space of all possible histories.


## Quantum gravity

Whereas in quantum mechanics the path integral formulation is fully equivalent to other formulations, it may be that it can be extended to quantum gravity, which would make it different from the Hilbert space model. Feynman had some success in this direction, and his work has been extended by Hawking and others. Approaches that use this method include causal dynamical triangulations and spinfoam models.


## Quantum tunneling

Quantum tunnelling can be modeled by using the path integral formation to determine the action of the trajectory through a potential barrier. Using the WKB approximation, the tunneling rate (Γ) can be determined to be of the form

$\Gamma =A_{\mathrm {o} }\exp \left(-{\frac {S_{\mathrm {eff} }}{\hbar }}\right)$

with the effective action *S*eff and pre-exponential factor *A*o. This form is specifically useful in a dissipative system, in which the systems and surroundings must be modeled together. Using the Langevin equation to model Brownian motion, the path integral formation can be used to determine an effective action and pre-exponential model to see the effect of dissipation on tunnelling. From this model, tunneling rates of macroscopic systems (at finite temperatures) can be predicted.
