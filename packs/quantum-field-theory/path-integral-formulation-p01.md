---
title: "Path-integral formulation (part 1/2)"
source: https://en.wikipedia.org/wiki/Path_integral_formulation
domain: quantum-field-theory
license: CC-BY-SA-4.0
tags: quantum field theory, gauge theory, feynman diagram, path integral formulation
fetched: 2026-07-02
part: 1/2
---

# Path-integral formulation

(Redirected from

Path integral formulation

)

The **path-integral formulation** of quantum mechanics generalizes the action principle of classical mechanics. It replaces the classical notion of a single, unique classical trajectory for a system with a sum, or functional integral, over an infinity of quantum-mechanically possible trajectories to compute a quantum amplitude.

This formulation has proven crucial to the subsequent development of theoretical physics, because manifest Lorentz covariance (time and space components of quantities enter equations in the same way) is easier to achieve than in the operator formalism of canonical quantization. Unlike previous methods, the path integral allows one to easily change coordinates between very different canonical descriptions of the same quantum system. Another advantage is that it is in practice easier to guess the correct form of the Lagrangian of a theory, which naturally enters the path integrals (for interactions of a certain type, these are *coordinate-space*, or *Feynman path integrals*), than the Hamiltonian. Possible downsides of the approach include that unitarity (this is related to conservation of probability; the probabilities of all physically possible outcomes must add up to one) of the S-matrix is obscure in the formulation. The path-integral approach has proven to be equivalent to the other formalisms of quantum mechanics and quantum field theory. Thus, by *deriving* either approach from the other, problems associated with one or the other approach (as exemplified by Lorentz covariance or unitarity) go away.

The path integral also relates quantum and stochastic processes, and this provided the basis for the grand synthesis of the 1970s, which unified quantum field theory with the statistical field theory of a fluctuating field near a second-order phase transition. The Schrödinger equation is a diffusion equation with an imaginary diffusion constant, and the path integral is an analytic continuation of a method for summing up all possible random walks.

The path integral has impacted a wide array of sciences, including polymer physics, quantum field theory, string theory and cosmology. In physics, it is a foundation for lattice gauge theory and quantum chromodynamics. It has been called the "most powerful formula in physics", with Stephen Wolfram also declaring it to be the "fundamental mathematical construct of modern quantum mechanics and quantum field theory".

The basic idea of the path-integral formulation can be traced back to Norbert Wiener, who introduced the Wiener integral for solving problems in diffusion and Brownian motion. This idea was extended to the use of the Lagrangian in quantum mechanics by Paul Dirac, whose 1933 paper gave birth to path-integral formulation. The complete method was developed in 1948 by Richard Feynman. Some preliminaries were worked out earlier in his doctoral work under the supervision of John Archibald Wheeler. The original motivation stemmed from the desire to obtain a quantum-mechanical formulation for the Wheeler–Feynman absorber theory using a Lagrangian (rather than a Hamiltonian) as a starting point.


## Quantum action principle

In quantum mechanics, as in classical mechanics, the Hamiltonian is the generator of time translations. This means that the state at a slightly later time differs from the state at the current time by the result of acting with the Hamiltonian operator (multiplied by the negative imaginary unit, −*i*). For states with a definite energy, this is a statement of the de Broglie relation between frequency and energy, and the general relation is consistent with that plus the superposition principle.

The Hamiltonian in classical mechanics is derived from a Lagrangian, which is a more fundamental quantity in the context of special relativity. The Hamiltonian indicates how to march forward in time, but the time is different in different reference frames. The Lagrangian is a Lorentz scalar, while the Hamiltonian is the time component of a four-vector. So the Hamiltonian is different in different frames, and this type of symmetry is not apparent in the original formulation of quantum mechanics.

The Hamiltonian is a function of the position and momentum at one time, and it determines the position and momentum a little later. The Lagrangian is a function of the position now and the position a little later (or, equivalently for infinitesimal time separations, it is a function of the position and velocity). The relation between the two is by a Legendre transformation, and the condition that determines the classical equations of motion (the Euler–Lagrange equations) is that the action has an extremum.

In quantum mechanics, the Legendre transform is hard to interpret, because the motion is not over a definite trajectory. In classical mechanics, with discretization in time, the Legendre transform becomes

$\varepsilon H=p(t){\big (}q(t+\varepsilon )-q(t){\big )}-\varepsilon L$

and

$p={\frac {\partial L}{\partial {\dot {q}}}},$

where the partial derivative with respect to ${\dot {q}}$ holds *q*(*t* + *ε*) fixed. The inverse Legendre transform is

$\varepsilon L=\varepsilon p{\dot {q}}-\varepsilon H,$

where

${\dot {q}}={\frac {\partial H}{\partial p}},$

and the partial derivative now is with respect to p at fixed q.

In quantum mechanics, the state is a superposition of different states with different values of q, or different values of p, and the quantities p and q can be interpreted as noncommuting operators. The operator p is only definite on states that are indefinite with respect to q. So consider two states separated in time and act with the operator corresponding to the Lagrangian:

$e^{i{\big [}p{\big (}q(t+\varepsilon )-q(t){\big )}-\varepsilon H(p,q){\big ]}}.$

If the multiplications implicit in this formula are reinterpreted as *matrix* multiplications, the first factor is

$e^{-ipq(t)},$

and if this is also interpreted as a matrix multiplication, the sum over all states integrates over all *q*(*t*), and so it takes the Fourier transform in *q*(*t*) to change basis to *p*(*t*). That is the action on the Hilbert space – *change basis to p at time t*.

Next comes

$e^{-i\varepsilon H(p,q)},$

or *evolve an infinitesimal time into the future*.

Finally, the last factor in this interpretation is

$e^{ipq(t+\varepsilon )},$

which means *change basis back to q at a later time*.

This is not very different from just ordinary time evolution: the H factor contains all the dynamical information – it pushes the state forward in time. The first part and the last part are just Fourier transforms to change to a pure q basis from an intermediate p basis.

Another way of saying this is that since the Hamiltonian is naturally a function of p and q, exponentiating this quantity and changing basis from p to q at each step allows the matrix element of H to be expressed as a simple function along each path. This function is the quantum analog of the classical action. This observation is due to Paul Dirac.

Dirac further noted that one could square the time-evolution operator in the S representation:

$e^{i\varepsilon S},$

and this gives the time-evolution operator between time t and time *t* + 2*ε*. In the H representation, the quantity summed over the intermediate states corresponds to a matrix element that is not directly observable. In contrast, in the S representation, this quantity is interpreted as being associated with a path. Taking a large power of this operator reconstructs the full quantum evolution between two states: the initial state with a fixed value of *q*(*0*) and the final state with a fixed value of *q*(*t*). The resulting expression can be understood as a sum over paths, where each path contributes a phase given by the quantum action.


## Classical limit

Crucially, Dirac identified the effect of the classical limit on the quantum form of the action principle:

> ...we see that the integrand in (11) must be of the form *e**iF*/*h*, where F is a function of *q**T*, *q*1, *q*2, … *q**m*, *q**t*, which remains finite as h tends to zero. Let us now picture one of the intermediate qs, say qk, as varying continuously while the other ones are fixed. Owing to the smallness of h, we shall then in general have *F*/*h* varying extremely rapidly. This means that *e**iF*/*h* will vary periodically with a very high frequency about the value zero, as a result of which its integral will be practically zero. The only important part in the domain of integration of qk is thus that for which a comparatively large variation in qk produces only a very small variation in F. This part is the neighbourhood of a point for which F is stationary with respect to small variations in qk. We can apply this argument to each of the variables of integration ... and obtain the result that the only important part in the domain of integration is that for which F is stationary for small variations in all intermediate qs. ... We see that F has for its classical analogue ∫*t* *T* *L dt*, which is just the action function, which classical mechanics requires to be stationary for small variations in all the intermediate qs. This shows the way in which equation (11) goes over into classical results when h becomes extremely small.

— Dirac (1933), p. 69

That is, in the limit of action that is large compared to the Planck constant ħ – the classical limit – the path integral is dominated by solutions that are in the neighborhood of stationary points of the action. The classical path arises naturally in the classical limit.


## Feynman's interpretation

Dirac's work did not provide a precise prescription to calculate the sum over paths, and he did not show that one could recover the Schrödinger equation or the canonical commutation relations from this rule. This was done by Feynman.

Feynman showed that Dirac's quantum action was, for most cases of interest, simply equal to the classical action, appropriately discretized. This means that the classical action is the phase acquired by quantum evolution between two fixed endpoints. He proposed to recover all of quantum mechanics from the following postulates:

1. The probability for an event is given by the squared modulus of a complex number called the "probability amplitude".
2. The probability amplitude is given by adding together the contributions of all paths in configuration space.
3. The contribution of a path is proportional to *e**iS*/*ħ*, where S is the action given by the time integral of the Lagrangian along the path.

In order to find the overall probability amplitude for a given process, then, one adds up, or integrates, the amplitude of the 3rd postulate over the space of *all* possible paths of the system in between the initial and final states, including those that are absurd by classical standards. In calculating the probability amplitude for a single particle to go from one space-time coordinate to another, it is correct to include paths in which the particle describes elaborate curlicues, curves in which the particle shoots off into outer space and flies back again, and so forth. The **path integral** assigns to all these amplitudes *equal weight* but varying phase, or argument of the complex number. Contributions from paths wildly different from the classical trajectory may be suppressed by interference (see below).

Feynman showed that this formulation of quantum mechanics is equivalent to the canonical approach to quantum mechanics when the Hamiltonian is at most quadratic in the momentum. An amplitude computed according to Feynman's principles will also obey the Schrödinger equation for the Hamiltonian corresponding to the given action.

The path integral formulation of quantum field theory represents the transition amplitude (corresponding to the classical correlation function) as a weighted sum of all possible histories of the system from the initial to the final state. A Feynman diagram is a graphical representation of a perturbative contribution to the transition amplitude.


## Path integral in quantum mechanics

### Time-slicing derivation

One common approach to deriving the path integral formula is to divide the time interval into small pieces. Once this is done, the Trotter product formula tells us that the noncommutativity of the kinetic and potential energy operators can be ignored.

For a particle in a smooth potential, the path integral is approximated by zigzag paths, which in one dimension is a product of ordinary integrals. For the motion of the particle from position xa at time ta to xb at time tb, the time sequence

$t_{a}=t_{0}<t_{1}<\cdots <t_{n-1}<t_{n}<t_{n+1}=t_{b}$

can be divided up into *n* + 1 smaller segments *tj* − *t**j* − 1, where *j* = 1, ..., *n* + 1, of fixed duration

$\varepsilon =\Delta t={\frac {t_{b}-t_{a}}{n+1}}.$

This process is called *time-slicing*.

An approximation for the path integral can be computed as proportional to

$\int \limits _{-\infty }^{+\infty }\cdots \int \limits _{-\infty }^{+\infty }\exp \left({\frac {i}{\hbar }}\int _{t_{a}}^{t_{b}}L{\big (}x(t),v(t){\big )}\,dt\right)\,dx_{0}\,\cdots \,dx_{n},$

where *L*(*x*, *v*) is the Lagrangian of the one-dimensional system with position variable *x*(*t*) and velocity *v* = *ẋ*(*t*) considered (see below), and dxj corresponds to the position at the jth time step, if the time integral is approximated by a sum of n terms.

In the limit *n* → ∞, this becomes a functional integral, which, apart from a nonessential factor, is directly the product of the probability amplitudes ⟨*xb*, *tb*|*xa*, *ta*⟩ (more precisely, since one must work with a continuous spectrum, the respective densities) to find the quantum mechanical particle at ta in the initial state xa and at tb in the final state xb.

Actually L is the classical Lagrangian of the one-dimensional system considered,

$L(x,{\dot {x}})=T-V={\frac {1}{2}}m|{\dot {x}}|^{2}-V(x)$

and the abovementioned "zigzagging" corresponds to the appearance of the terms

$\exp \left({\frac {i}{\hbar }}\varepsilon \sum _{j=1}^{n+1}L\left({\tilde {x}}_{j},{\frac {x_{j}-x_{j-1}}{\varepsilon }},j\right)\right)$

in the Riemann sum approximating the time integral, which are finally integrated over *x*1 to xn with the integration measure *dx*1...*dxn*, x̃j is an arbitrary value of the interval corresponding to j, e.g. its center, ⁠*xj* + *x**j*−1/2⁠.

Thus, in contrast to classical mechanics, not only does the stationary path contribute, but actually all virtual paths between the initial and the final point also contribute.

### Path integral

In terms of the wave function in the position representation, the path integral formula reads as follows:

$\psi (x,t)={\frac {1}{Z}}\int _{\mathbf {x} (0)=x}{\mathcal {D}}\mathbf {x} \,e^{iS[\mathbf {x} ,{\dot {\mathbf {x} }}]}\psi _{0}(\mathbf {x} (t))\,$

where ${\mathcal {D}}\mathbf {x}$ denotes integration over all paths $\mathbf {x}$ with $\mathbf {x} (0)=x$ and where Z is a normalization factor. Here S is the action, given by

$S[\mathbf {x} ,{\dot {\mathbf {x} }}]=\int dt\,L(\mathbf {x} (t),{\dot {\mathbf {x} }}(t))$

### Free particle

The path integral representation gives the quantum amplitude to go from point x to point y as an integral over all paths. For a free-particle action (for simplicity let *m* = 1, *ħ* = 1)

$S=\int {\frac {{\dot {x}}^{2}}{2}}\,\mathrm {d} t,$

the integral can be evaluated explicitly.

To do this, it is convenient to start without the factor i in the exponential, so that large deviations are suppressed by small numbers, not by cancelling oscillatory contributions. The amplitude (or Kernel) reads:

$K(x-y;T)=\int _{x(0)=x}^{x(T)=y}\exp \left(-\int _{0}^{T}{\frac {{\dot {x}}^{2}}{2}}\,\mathrm {d} t\right)\,{\mathcal {D}}x.$

Splitting the integral into time slices:

$K(x-y;T)=\int _{x(0)=x}^{x(T)=y}\prod _{t}\exp \left(-{\tfrac {1}{2}}\left({\frac {x(t+\varepsilon )-x(t)}{\varepsilon }}\right)^{2}\varepsilon \right)\,{\mathcal {D}}x,$

where the D is interpreted as a finite collection of integrations at each integer multiple of ε. Each factor in the product is a Gaussian as a function of *x*(*t* + *ε*) centered at *x*(*t*) with variance ε. The multiple integrals are a repeated convolution of this Gaussian Gε with copies of itself at adjacent times:

$K(x-y;T)=G_{\varepsilon }*G_{\varepsilon }*\cdots *G_{\varepsilon },$

where the number of convolutions is ⁠*T*/*ε*⁠. The result is easy to evaluate by taking the Fourier transform of both sides, so that the convolutions become multiplications:

${\tilde {K}}(p;T)={\tilde {G}}_{\varepsilon }(p)^{T/\varepsilon }.$

The Fourier transform of the Gaussian G is another Gaussian of reciprocal variance:

${\tilde {G}}_{\varepsilon }(p)=e^{-{\frac {\varepsilon p^{2}}{2}}},$

and the result is

${\tilde {K}}(p;T)=e^{-{\frac {Tp^{2}}{2}}}.$

The Fourier transform gives K, and it is a Gaussian again with reciprocal variance:

$K(x-y;T)\propto e^{-{\frac {(x-y)^{2}}{2T}}}.$

The proportionality constant is not really determined by the time-slicing approach, only the ratio of values for different endpoint choices is determined. The proportionality constant should be chosen to ensure that between each two time slices the time evolution is quantum-mechanically unitary, but a more illuminating way to fix the normalization is to consider the path integral as a description of a stochastic process.

The result has a probability interpretation. The sum over all paths of the exponential factor can be seen as the sum over each path of the probability of selecting that path. The probability is the product over each segment of the probability of selecting that segment, so that each segment is probabilistically independently chosen. The fact that the answer is a Gaussian spreading linearly in time is the central limit theorem, which can be interpreted as the first historical evaluation of a statistical path integral.

The probability interpretation gives a natural normalization choice. The path integral should be defined so that

$\int K(x-y;T)\,dy=1.$

This condition normalizes the Gaussian and produces a kernel that obeys the diffusion equation:

${\frac {d}{dt}}K(x;T)={\frac {\nabla ^{2}}{2}}K.$

For oscillatory path integrals, ones with an i in the numerator, the time slicing produces convolved Gaussians, just as before. Now, however, the convolution product is marginally singular, since it requires careful limits to evaluate the oscillating integrals. To make the factors well defined, the easiest way is to add a small imaginary part to the time increment ε. This is closely related to Wick rotation. Then the same convolution argument as before gives the propagation kernel:

$K(x-y;T)\propto e^{\frac {i(x-y)^{2}}{2T}},$

which, with the same normalization as before (not the sum-squares normalization – this function has a divergent norm), obeys a free Schrödinger equation:

${\frac {d}{dt}}K(x;T)=i{\frac {\nabla ^{2}}{2}}K.$

This means that any superposition of Ks will also obey the same equation, by linearity. Defining

$\psi _{t}(y)=\int \psi _{0}(x)K(x-y;t)\,dx=\int \psi _{0}(x)\int _{x(0)=x}^{x(t)=y}e^{iS}\,{\mathcal {D}}x,$

then ψt obeys the free Schrödinger equation just as K does:

$i{\frac {\partial }{\partial t}}\psi _{t}=-{\frac {\nabla ^{2}}{2}}\psi _{t}.$

### Simple harmonic oscillator

The Lagrangian for the simple harmonic oscillator is

${\mathcal {L}}={\tfrac {1}{2}}m{\dot {x}}^{2}-{\tfrac {1}{2}}m\omega ^{2}x^{2}.$

Write its trajectory *x*(*t*) as the classical trajectory plus some perturbation, *x*(*t*) = *x*c(*t*) + *δx*(*t*) and the action as *S* = *S*c + *δS*. The classical trajectory can be written as

$x_{\text{c}}(t)=x_{i}{\frac {\sin \omega (t_{f}-t)}{\sin \omega (t_{f}-t_{i})}}+x_{f}{\frac {\sin \omega (t-t_{i})}{\sin \omega (t_{f}-t_{i})}}.$

This trajectory yields the classical action

${\begin{aligned}S_{\text{c}}&=\int _{t_{i}}^{t_{f}}{\mathcal {L}}\,dt=\int _{t_{i}}^{t_{f}}\left({\tfrac {1}{2}}m{\dot {x}}^{2}-{\tfrac {1}{2}}m\omega ^{2}x^{2}\right)\,dt\\[6pt]&={\frac {1}{2}}m\omega \left({\frac {(x_{i}^{2}+x_{f}^{2})\cos \omega (t_{f}-t_{i})-2x_{i}x_{f}}{\sin \omega (t_{f}-t_{i})}}\right)~.\end{aligned}}$

Next, expand the deviation from the classical path as a Fourier series, and calculate the contribution to the action δS, which gives

$S=S_{\text{c}}+\sum _{n=1}^{\infty }{\tfrac {1}{2}}a_{n}^{2}{\frac {m}{2}}\left({\frac {(n\pi )^{2}}{t_{f}-t_{i}}}-\omega ^{2}(t_{f}-t_{i})\right).$

This means that the propagator is

${\begin{aligned}K(x_{f},t_{f};x_{i},t_{i})&=Qe^{\frac {iS_{\text{c}}}{\hbar }}\prod _{j=1}^{\infty }{\frac {j\pi }{\sqrt {2}}}\int da_{j}\exp {\left({\frac {i}{2\hbar }}a_{j}^{2}{\frac {m}{2}}\left({\frac {(j\pi )^{2}}{t_{f}-t_{i}}}-\omega ^{2}(t_{f}-t_{i})\right)\right)}\\[6pt]&=e^{\frac {iS_{\text{c}}}{\hbar }}Q\prod _{j=1}^{\infty }\left(1-\left({\frac {\omega (t_{f}-t_{i})}{j\pi }}\right)^{2}\right)^{-{\frac {1}{2}}}\end{aligned}}$

for some normalization

$Q={\sqrt {\frac {m}{2\pi i\hbar (t_{f}-t_{i})}}}~.$

Using the infinite-product representation of the sinc function,

$\prod _{j=1}^{\infty }\left(1-{\frac {x^{2}}{j^{2}}}\right)={\frac {\sin \pi x}{\pi x}},$

the propagator can be written as

$K(x_{f},t_{f};x_{i},t_{i})=Qe^{\frac {iS_{\text{c}}}{\hbar }}{\sqrt {\frac {\omega (t_{f}-t_{i})}{\sin \omega (t_{f}-t_{i})}}}=e^{\frac {iS_{c}}{\hbar }}{\sqrt {\frac {m\omega }{2\pi i\hbar \sin \omega (t_{f}-t_{i})}}}.$

Let *T* = *tf* − *ti*. One may write this propagator in terms of energy eigenstates as

${\begin{aligned}K(x_{f},t_{f};x_{i},t_{i})&=\left({\frac {m\omega }{2\pi i\hbar \sin \omega T}}\right)^{\frac {1}{2}}\exp {\left({\frac {i}{\hbar }}{\tfrac {1}{2}}m\omega {\frac {(x_{i}^{2}+x_{f}^{2})\cos \omega T-2x_{i}x_{f}}{\sin \omega T}}\right)}\\[6pt]&=\sum _{n=0}^{\infty }\exp {\left(-{\frac {iE_{n}T}{\hbar }}\right)}\psi _{n}(x_{f})\psi _{n}(x_{i})^{*}~.\end{aligned}}$

Using the identities *i* sin *ωT* = ⁠1/2⁠*e**iωT* (1 − *e*−2*iωT*) and cos *ωT* = ⁠1/2⁠*e**iωT* (1 + *e*−2*iωT*), this amounts to

$K(x_{f},t_{f};x_{i},t_{i})=\left({\frac {m\omega }{\pi \hbar }}\right)^{\frac {1}{2}}e^{\frac {-i\omega T}{2}}\left(1-e^{-2i\omega T}\right)^{-{\frac {1}{2}}}\exp {\left(-{\frac {m\omega }{2\hbar }}\left(\left(x_{i}^{2}+x_{f}^{2}\right){\frac {1+e^{-2i\omega T}}{1-e^{-2i\omega T}}}-{\frac {4x_{i}x_{f}e^{-i\omega T}}{1-e^{-2i\omega T}}}\right)\right)}.$

One may absorb all terms after the first *e*−*iωT*/2 into *R*(*T*), thereby obtaining

$K(x_{f},t_{f};x_{i},t_{i})=\left({\frac {m\omega }{\pi \hbar }}\right)^{\frac {1}{2}}e^{\frac {-i\omega T}{2}}\cdot R(T).$

One may finally expand *R*(*T*) in powers of *e*−*iωT*: All terms in this expansion get multiplied by the *e*−*iωT*/2 factor in the front, yielding terms of the form

$e^{\frac {-i\omega T}{2}}e^{-in\omega T}=e^{-i\omega T\left({\frac {1}{2}}+n\right)}\quad {\text{for }}n=0,1,2,\ldots .$

Comparison to the above eigenstate expansion yields the standard energy spectrum for the simple harmonic oscillator,

$E_{n}=\left(n+{\tfrac {1}{2}}\right)\hbar \omega ~.$

### Coulomb potential

Feynman's time-sliced approximation does not, however, exist for the most important quantum-mechanical path integrals of atoms, due to the singularity of the Coulomb potential ⁠*e*2/*r*⁠ at the origin. Only after replacing the time t by another path-dependent pseudo-time parameter

$s=\int {\frac {dt}{r(t)}}$

the singularity is removed and a time-sliced approximation exists, which is exactly integrable, since it can be made harmonic by a simple coordinate transformation, as discovered in 1979 by İsmail Hakkı Duru and Hagen Kleinert. The combination of a path-dependent time transformation and a coordinate transformation is an important tool to solve many path integrals and is called generically the Duru–Kleinert transformation.

### The Schrödinger equation

The path integral reproduces the Schrödinger equation for the initial and final state even when a potential is present. This is easiest to see by taking a path-integral over infinitesimally separated times.

$\psi (y;t+\varepsilon )=\int _{-\infty }^{\infty }\psi (x;t)\int _{x(t)=x}^{x(t+\varepsilon )=y}e^{i\int _{t}^{t+\varepsilon }{\bigl (}{\frac {1}{2}}{\dot {x}}^{2}-V(x){\bigr )}dt}Dx(t)\,dx\qquad (1)$

Since the time separation is infinitesimal and the cancelling oscillations become severe for large values of ẋ, the path integral has most weight for y close to x. In this case, to lowest order the potential energy is constant, and only the kinetic energy contribution is nontrivial. (This separation of the kinetic and potential energy terms in the exponent is essentially the Trotter product formula.) The exponential of the action is

$e^{-i\varepsilon V(x)}e^{i{\frac {{\dot {x}}^{2}}{2}}\varepsilon }$

The first term rotates the phase of *ψ*(*x*) locally by an amount proportional to the potential energy. The second term is the free particle propagator, corresponding to i times a diffusion process. To lowest order in ε they are additive; in any case one has with (1):

$\psi (y;t+\varepsilon )\approx \int \psi (x;t)e^{-i\varepsilon V(x)}e^{\frac {i(x-y)^{2}}{2\varepsilon }}\,dx\,.$

As mentioned, the spread in ψ is diffusive from the free particle propagation, with an extra infinitesimal rotation in phase that slowly varies from point to point from the potential:

${\frac {\partial \psi }{\partial t}}=i\cdot \left({\tfrac {1}{2}}\nabla ^{2}-V(x)\right)\psi \,$

and this is the Schrödinger equation. The normalization of the path integral needs to be fixed in exactly the same way as in the free particle case. An arbitrary continuous potential does not affect the normalization, although singular potentials require careful treatment.

### Equations of motion

Since the states obey the Schrödinger equation, the path integral must reproduce the Heisenberg equations of motion for the averages of x and ẋ variables, but it is instructive to see this directly. The direct approach shows that the expectation values calculated from the path integral reproduce the usual ones of quantum mechanics.

Start by considering the path integral with some fixed initial state

$\int \psi _{0}(x)\int _{x(0)=x}e^{iS(x,{\dot {x}})}\,Dx\,$

Now *x*(*t*) at each separate time is a separate integration variable. So it is legitimate to change variables in the integral by shifting: *x*(*t*) = *u*(*t*) + *ε*(*t*) where *ε*(*t*) is a different shift at each time but *ε*(0) = *ε*(*T*) = 0, since the endpoints are not integrated:

$\int \psi _{0}(x)\int _{u(0)=x}e^{iS(u+\varepsilon ,{\dot {u}}+{\dot {\varepsilon }})}\,Du\,$

The change in the integral from the shift is, to first infinitesimal order in ε:

$\int \psi _{0}(x)\int _{u(0)=x}\left(\int {\frac {\partial S}{\partial u}}\varepsilon +{\frac {\partial S}{\partial {\dot {u}}}}{\dot {\varepsilon }}\,dt\right)e^{iS}\,Du\,$

which, integrating by parts in t, gives:

$\int \psi _{0}(x)\int _{u(0)=x}-\left(\int \left({\frac {d}{dt}}{\frac {\partial S}{\partial {\dot {u}}}}-{\frac {\partial S}{\partial u}}\right)\varepsilon (t)\,dt\right)e^{iS}\,Du\,$

But this was just a shift of integration variables, which doesn't change the value of the integral for any choice of *ε*(*t*). The conclusion is that this first order variation is zero for an arbitrary initial state and at any arbitrary point in time:

$\left\langle \psi _{0}\left|{\frac {\delta S}{\delta x}}(t)\right|\psi _{0}\right\rangle =0$

this is the Heisenberg equation of motion.

If the action contains terms that multiply ẋ and x, at the same moment in time, the manipulations above are only heuristic, because the multiplication rules for these quantities is just as noncommuting in the path integral as it is in the operator formalism.

### Stationary-phase approximation

If the variation in the action exceeds ħ by many orders of magnitude, we typically have destructive interference other than in the vicinity of those trajectories satisfying the Euler–Lagrange equation, which is now reinterpreted as the condition for constructive interference. This can be shown using the method of stationary phase applied to the propagator. As ħ decreases, the exponential in the integral oscillates rapidly in the complex domain for any change in the action. Thus, in the limit that ħ goes to zero, only points where the classical action does not vary contribute to the propagator.

### Canonical commutation relations

The formulation of the path integral does not make it clear at first sight that the quantities x and p do not commute. In the path integral, these are just integration variables and they have no obvious ordering. Feynman discovered that the non-commutativity is still present.

To see this, consider the simplest path integral, the brownian walk. This is not yet quantum mechanics, so in the path-integral the action is not multiplied by i:

$S=\int \left({\frac {dx}{dt}}\right)^{2}\,dt$

The quantity *x*(*t*) is fluctuating, and the derivative is defined as the limit of a discrete difference.

${\frac {dx}{dt}}={\frac {x(t+\varepsilon )-x(t)}{\varepsilon }}$

The distance that a random walk moves is proportional to √*t*, so that:

$x(t+\varepsilon )-x(t)\approx {\sqrt {\varepsilon }}$

This shows that the random walk is not differentiable, since the ratio that defines the derivative diverges with probability one.

The quantity xẋ is ambiguous, with two possible meanings:

$[1]=x{\frac {dx}{dt}}=x(t){\frac {x(t+\varepsilon )-x(t)}{\varepsilon }}$

$[2]=x{\frac {dx}{dt}}=x(t+\varepsilon ){\frac {x(t+\varepsilon )-x(t)}{\varepsilon }}$

In elementary calculus, the two are only different by an amount that goes to 0 as ε goes to 0. But in this case, the difference between the two is not 0:

$[2]-[1]={\frac {{\big (}x(t+\varepsilon )-x(t){\big )}^{2}}{\varepsilon }}\approx {\frac {\varepsilon }{\varepsilon }}$

Let

$f(t)={\frac {{\big (}x(t+\varepsilon )-x(t){\big )}^{2}}{\varepsilon }}$

Then *f*(*t*) is a rapidly fluctuating statistical quantity, whose average value is 1, i.e. a normalized "Gaussian process". The fluctuations of such a quantity can be described by a statistical Lagrangian

${\mathcal {L}}=(f(t)-1)^{2}\,,$

and the equations of motion for f derived from extremizing the action S corresponding to L just set it equal to 1. In physics, such a quantity is "equal to 1 as an operator identity". In mathematics, it "weakly converges to 1". In either case, it is 1 in any expectation value, or when averaged over any interval, or for all practical purpose.

Defining the time order to *be* the operator order:

$[x,{\dot {x}}]=x{\frac {dx}{dt}}-{\frac {dx}{dt}}x=1$

This is called the Itō lemma in stochastic calculus, and the (euclideanized) canonical commutation relations in physics.

For a general statistical action, a similar argument shows that

$\left[x,{\frac {\partial S}{\partial {\dot {x}}}}\right]=1$

and in quantum mechanics, the extra imaginary unit in the action converts this to the canonical commutation relation,

$[x,p]=i$

### Particle in curved space

For a particle in curved space the kinetic term depends on the position, and the above time slicing cannot be applied, this being a manifestation of the notorious operator ordering problem in Schrödinger quantum mechanics. One may, however, solve this problem by transforming the time-sliced flat-space path integral to curved space using a multivalued coordinate transformation (nonholonomic mapping explained here).

### Measure-theoretic factors

Sometimes (e.g. a particle moving in curved space) we also have measure-theoretic factors in the functional integral:

$\int \mu [x]e^{iS[x]}\,{\mathcal {D}}x.$

This factor is needed to restore unitarity.

For instance, if

$S=\int \left({\frac {m}{2}}g_{ij}{\dot {x}}^{i}{\dot {x}}^{j}-V(x)\right)\,dt,$

then it means that each spatial slice is multiplied by the measure √*g*. This measure cannot be expressed as a functional multiplying the D*x* measure because they belong to entirely different classes.

### Expectation values and matrix elements

Matrix elements of the kind $\langle x_{f}|e^{-{\frac {i}{\hbar }}{\hat {H}}(t-t')}F({\hat {x}})e^{-{\frac {i}{\hbar }}{\hat {H}}(t')}|x_{i}\rangle$ take the form

$\int _{x(0)=x_{i}}^{x(t)=x_{f}}{\mathcal {D}}[x]F(x(t'))e^{{\frac {i}{\hbar }}\int dtL(x(t),{\dot {x}}(t))}$

.

This generalizes to multiple operators, for example

$\langle x_{f}|e^{-{\frac {i}{\hbar }}{\hat {H}}(t-t_{1})}F_{1}({\hat {x}})e^{-{\frac {i}{\hbar }}{\hat {H}}(t_{1}-t_{2})}F_{2}({\hat {x}})e^{-{\frac {i}{\hbar }}{\hat {H}}(t_{2})}|x_{i}\rangle =\int _{x(0)=x_{i}}^{x(t)=x_{f}}{\mathcal {D}}[x]F_{1}(x(t_{1}))F_{2}(x(t_{2}))e^{{\frac {i}{\hbar }}\int dtL(x(t),{\dot {x}}(t))}$

,

and to the general vacuum expectation value (in the large time limit)

$\langle F\rangle ={\frac {\int {\mathcal {D}}[\phi ]F(\phi )e^{{\frac {i}{\hbar }}S[\phi ]}}{\int {\mathcal {D}}[\phi ]e^{{\frac {i}{\hbar }}S[\phi ]}}}$

.


## Euclidean path integrals

It is very common in path integrals to perform a Wick rotation from real to imaginary times. In the setting of quantum field theory, the Wick rotation changes the geometry of space-time from Lorentzian to Euclidean; as a result, Wick-rotated path integrals are often called Euclidean path integrals.

### Wick rotation and the Feynman–Kac formula

If we replace t by $-it$ , the time-evolution operator $e^{-it{\hat {H}}/\hbar }$ is replaced by $e^{-t{\hat {H}}/\hbar }$ . (This change is known as a Wick rotation.) If we repeat the derivation of the path-integral formula in this setting, we obtain

$\psi (x,t)={\frac {1}{Z}}\int _{\mathbf {x} (0)=x}e^{-S_{\mathrm {Euclidean} }(\mathbf {x} ,{\dot {\mathbf {x} }})/\hbar }\psi _{0}(\mathbf {x} (t))\,{\mathcal {D}}\mathbf {x} \,$

,

where $S_{\mathrm {Euclidean} }$ is the Euclidean action, given by

$S_{\mathrm {Euclidean} }(\mathbf {x} ,{\dot {\mathbf {x} }})=\int \left[{\frac {m}{2}}|{\dot {\mathbf {x} }}(t)|^{2}+V(\mathbf {x} (t))\right]\,dt$

.

Note the sign change between this and the normal action, where the potential energy term is negative. (The term *Euclidean* is from the context of quantum field theory, where the change from real to imaginary time changes the space-time geometry from Lorentzian to Euclidean.)

Now, the contribution of the kinetic energy to the path integral is as follows:

${\frac {1}{Z}}\int _{\mathbf {x} (0)=x}f(\mathbf {x} )e^{-{\frac {m}{2}}\int |{\dot {\mathbf {x} }}|^{2}dt}\,{\mathcal {D}}\mathbf {x} \,$

where $f(\mathbf {x} )$ includes all the remaining dependence of the integrand on the path. This integral has a rigorous mathematical interpretation as integration against the Wiener measure, denoted $\mu _{x}$ . The Wiener measure, constructed by Norbert Wiener gives a rigorous foundation to Einstein's mathematical model of Brownian motion. The subscript x indicates that the measure $\mu _{x}$ is supported on paths $\mathbf {x}$ with $\mathbf {x} (0)=x$ .

We then have a rigorous version of the Feynman path integral, known as the Feynman–Kac formula:

$\psi (x,t)=\int e^{-\int V(\mathbf {x} (t))\,dt/\hbar }\,\psi _{0}(\mathbf {x} (t))\,d\mu _{x}(\mathbf {x} )$

,

where now $\psi (x,t)$ satisfies the Wick-rotated version of the Schrödinger equation,

$\hbar {\frac {\partial }{\partial t}}\psi (x,t)=-{\hat {H}}\psi (x,t)$

.

Although the Wick-rotated Schrödinger equation does not have a direct physical meaning, interesting properties of the Schrödinger operator ${\hat {H}}$ can be extracted by studying it.

Much of the study of quantum field theories from the path-integral perspective, in both the mathematics and physics literatures, is done in the Euclidean setting, that is, after a Wick rotation. In particular, there are various results showing that if a Euclidean field theory with suitable properties can be constructed, one can then undo the Wick rotation to recover the physical, Lorentzian theory. On the other hand, it is much more difficult to give a meaning to path integrals (even Euclidean path integrals) in quantum field theory than in quantum mechanics.

### Path integral and the partition function

The path integral is just the generalization of the integral above to all quantum mechanical problems—

$Z=\int e^{\frac {i{\mathcal {S}}[\mathbf {x} ]}{\hbar }}\,{\mathcal {D}}\mathbf {x} \quad {\text{where }}{\mathcal {S}}[\mathbf {x} ]=\int _{0}^{t_{f}}L[\mathbf {x} (t),{\dot {\mathbf {x} }}(t)]\,dt$

is the action of the classical problem in which one investigates the path starting at time *t* = 0 and ending at time *t* = tf, and ${\mathcal {D}}\mathbf {x}$ denotes the integration measure over all paths. In the classical limit, ${\mathcal {S}}[\mathbf {x} ]\gg \hbar$ , the path of minimum action dominates the integral, because the phase of any path away from this fluctuates rapidly and different contributions cancel.

The connection with statistical mechanics follows. Considering only paths that begin and end in the same configuration, perform the Wick rotation *it* = *ħβ*, i.e., make time imaginary, and integrate over all possible beginning-ending configurations. The Wick-rotated path integral—described in the previous subsection, with the ordinary action replaced by its "Euclidean" counterpart—now resembles the partition function of statistical mechanics defined in a canonical ensemble with inverse temperature proportional to imaginary time, ⁠1/*T*⁠ = ⁠i*k*B*t*/*ħ*⁠. Strictly speaking, though, this is the partition function for a statistical field theory.

Clearly, such a deep analogy between quantum mechanics and statistical mechanics cannot be dependent on the formulation. In the canonical formulation, one sees that the unitary evolution operator of a state is given by

$|\alpha ;t\rangle =e^{-{\frac {iHt}{\hbar }}}|\alpha ;0\rangle$

where the state α is evolved from time *t* = 0. If one makes a Wick rotation here, and finds the amplitude to go from any state, back to the same state in (imaginary) time iβ is given by

$Z=\operatorname {Tr} \left[e^{-H\beta }\right]$

which is precisely the partition function of statistical mechanics for the same system at the temperature quoted earlier. One aspect of this equivalence was also known to Erwin Schrödinger who remarked that the equation named after him looked like the diffusion equation after Wick rotation. Note, however, that the Euclidean path integral is actually in the form of a *classical* statistical mechanics model.
