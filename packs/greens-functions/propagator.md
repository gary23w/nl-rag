---
title: "Propagator"
source: https://en.wikipedia.org/wiki/Propagator
domain: greens-functions
license: CC-BY-SA-4.0
tags: green's function, fundamental solution, method of images, propagator function
fetched: 2026-07-02
---

# Propagator

In quantum mechanics and quantum field theory, the **propagator** is a function that specifies the probability amplitude for a particle to travel from one place to another in a given period of time, or to travel with a certain energy and momentum. In Feynman diagrams, which serve to calculate the rate of collisions in quantum field theory, virtual particles contribute their propagator to the rate of the scattering event described by the respective diagram. Propagators may also be viewed as the inverse of the wave operator appropriate to the particle, and are, therefore, often called *(causal) Green's functions* (called "*causal*" to distinguish it from the elliptic Laplacian Green's function).

## Non-relativistic propagators

In non-relativistic quantum mechanics, the propagator gives the probability amplitude for a particle to travel from one spatial point (x') at one time (t') to another spatial point (x) at a later time (t).

The Green's function G for the Schrödinger equation is a function $G(x,t;x',t')={\frac {1}{i\hbar }}\Theta (t-t')K(x,t;x',t')$ satisfying $\left(i\hbar {\frac {\partial }{\partial t}}-H_{x}\right)G(x,t;x',t')=\delta (x-x')\delta (t-t'),$ where *H* denotes the Hamiltonian, *δ*(*x*) denotes the Dirac delta-function and Θ(*t*) is the Heaviside step function. The kernel of the above Schrödinger differential operator in the big parentheses is denoted by *K*(*x*, *t* ;*x′*, *t′*) and called the **propagator**.

This propagator may also be written as the transition amplitude $K(x,t;x',t')={\big \langle }x{\big |}U(t,t'){\big |}x'{\big \rangle },$ where *U*(*t*, *t′*) is the unitary time-evolution operator for the system taking states at time t′ to states at time t. Note the initial condition enforced by $\lim _{t\to t'}K(x,t;x',t')=\delta (x-x').$ The propagator may also be found by using a path integral:

$K(x,t;x',t')=\int \exp \left[{\frac {i}{\hbar }}\int _{t'}^{t}L({\dot {q}},q,t)\,dt\right]D[q(t)],$

where L denotes the Lagrangian and the boundary conditions are given by *q*(*t*) = *x*, *q*(*t′*) = *x′*. The paths that are summed over move only forwards in time and are integrated with the differential $D[q(t)]$ following the path in time.

The propagator lets one find the wave function of a system, given an initial wave function and a time interval. The new wave function is given by

$\psi (x,t)=\int _{-\infty }^{\infty }\psi (x',t')K(x,t;x',t')\,dx'.$

If *K*(*x*, *t*; *x*′, *t*′) only depends on the difference *x* − *x′*, this is a convolution of the initial wave function and the propagator.

### Examples

For a time-translationally invariant system, the propagator only depends on the time difference *t* − *t*′, so it may be rewritten as $K(x,t;x',t')=K(x,x';t-t').$

The propagator of a one-dimensional free particle, obtainable from, e.g., the path integral, is then

$K(x,x';t)={\frac {1}{2\pi }}\int _{-\infty }^{+\infty }dk\,e^{ik(x-x')}e^{-{\frac {i\hbar k^{2}t}{2m}}}=\left({\frac {m}{2\pi i\hbar t}}\right)^{\frac {1}{2}}e^{-{\frac {m(x-x')^{2}}{2i\hbar t}}}.$

Similarly, the propagator of a one-dimensional quantum harmonic oscillator is the Mehler kernel,

$K(x,x';t)=\left({\frac {m\omega }{2\pi i\hbar \sin \omega t}}\right)^{\frac {1}{2}}\exp \left(-{\frac {m\omega {\big (}(x^{2}+x'^{2})\cos \omega t-2xx'{\big )}}{2i\hbar \sin \omega t}}\right).$

The latter may be obtained from the previous free-particle result upon making use of van Kortryk's SU(1,1) Lie-group identity, ${\begin{aligned}&\exp \left(-{\frac {it}{\hbar }}\left({\frac {1}{2m}}{\mathsf {p}}^{2}+{\frac {1}{2}}m\omega ^{2}{\mathsf {x}}^{2}\right)\right)\\&=\exp \left(-{\frac {im\omega }{2\hbar }}{\mathsf {x}}^{2}\tan {\frac {\omega t}{2}}\right)\exp \left(-{\frac {i}{2m\omega \hbar }}{\mathsf {p}}^{2}\sin(\omega t)\right)\exp \left(-{\frac {im\omega }{2\hbar }}{\mathsf {x}}^{2}\tan {\frac {\omega t}{2}}\right),\end{aligned}}$ valid for operators ${\mathsf {x}}$ and ${\mathsf {p}}$ satisfying the Heisenberg relation $[{\mathsf {x}},{\mathsf {p}}]=i\hbar$ .

For the N-dimensional case, the propagator can be simply obtained by the product $K({\vec {x}},{\vec {x}}';t)=\prod _{q=1}^{N}K(x_{q},x_{q}';t).$

## Relativistic propagators

In relativistic quantum mechanics and quantum field theory the propagators are Lorentz-invariant. They give the amplitude for a particle to travel between two spacetime events.

### Scalar propagator

In quantum field theory, the theory of a free (or non-interacting) scalar field is a useful and simple example which serves to illustrate the concepts needed for more complicated theories. It describes spin-zero particles. There are a number of possible propagators for free scalar field theory. We now describe the most common ones.

### Position space

The position space propagators are Green's functions for the Klein–Gordon equation. This means that they are functions *G*(*x*, *y*) satisfying $\left(\square _{x}+m^{2}\right)G(x,y)=-\delta (x-y),$ where

- x, y are two points in Minkowski spacetime with metric signature (+, −, −, −),
- $\square _{x}={\tfrac {\partial ^{2}}{\partial t^{2}}}-\nabla ^{2}$ is the d'Alembertian operator acting on the x coordinates,
- *δ*(*x* − *y*) is the Dirac delta function.

(As typical in relativistic quantum field theory calculations, we use units where the speed of light c and the reduced Planck constant ħ are set to unity.)

We shall restrict attention to 4-dimensional Minkowski spacetime. We can perform a Fourier transform of the equation for the propagator, obtaining $\left(-p^{2}+m^{2}\right)G(p)=-1.$

This equation can be inverted in the sense of distributions, noting that the equation *xf*(*x*) = 1 has the solution (see Sokhotski–Plemelj theorem) $f(x)={\frac {1}{x\pm i\varepsilon }}={\frac {1}{x}}\mp i\pi \delta (x),$ with ε implying the limit to zero. Below, we discuss the right choice of the sign arising from causality requirements.

The solution is

$G(x,y)={\frac {1}{(2\pi )^{4}}}\int d^{4}p\,{\frac {e^{-ip(x-y)}}{p^{2}-m^{2}\pm i\varepsilon }},$

where $p(x-y):=p_{0}(x^{0}-y^{0})-{\vec {p}}\cdot ({\vec {x}}-{\vec {y}})$ is the 4-vector Minkowski inner product.

The different choices for how to deform the integration contour in the above expression lead to various forms for the propagator. The choice of contour is usually phrased in terms of the $p_{0}$ integral.

The integrand then has two poles at $p_{0}=\pm {\sqrt {{\vec {p}}^{2}+m^{2}}},$ so different choices of how to avoid these lead to different propagators.

### Causal propagators

#### Retarded propagator

A contour going clockwise over both poles gives the **causal retarded propagator**. This is zero if x-y is spacelike or y is to the future of x, so it is zero if *x* ⁰< *y* ⁰.

This choice of contour is equivalent to calculating the limit, $G_{\text{ret}}(x,y)=\lim _{\varepsilon \to 0}{\frac {1}{(2\pi )^{4}}}\int d^{4}p\,{\frac {e^{-ip(x-y)}}{(p_{0}+i\varepsilon )^{2}-{\vec {p}}^{2}-m^{2}}}=-{\frac {\Theta (x^{0}-y^{0})}{2\pi }}\delta (\tau _{xy}^{2})+\Theta (x^{0}-y^{0})\Theta (\tau _{xy}^{2}){\frac {mJ_{1}(m\tau _{xy})}{4\pi \tau _{xy}}}.$

Here $\Theta (x):={\begin{cases}1&x\geq 0\\0&x<0\end{cases}}$ is the Heaviside step function, $\tau _{xy}:={\sqrt {(x^{0}-y^{0})^{2}-({\vec {x}}-{\vec {y}})^{2}}}$ is the proper time from x to y, and $J_{1}$ is a Bessel function of the first kind. The propagator is non-zero only if $y\prec x$ , i.e., y causally precedes x, which, for Minkowski spacetime, means

$y^{0}\leq x^{0}$

and

$\tau _{xy}^{2}\geq 0~.$

This expression can be related to the vacuum expectation value of the commutator of the free scalar field operator, $G_{\text{ret}}(x,y)=-i\langle 0|\left[\Phi (x),\Phi (y)\right]|0\rangle \Theta (x^{0}-y^{0}),$ where $\left[\Phi (x),\Phi (y)\right]:=\Phi (x)\Phi (y)-\Phi (y)\Phi (x).$

#### Advanced propagator

A contour going anti-clockwise under both poles gives the **causal advanced propagator**. This is zero if x-y is spacelike or if y is to the past of x, so it is zero if *x* ⁰> *y* ⁰.

This choice of contour is equivalent to calculating the limit $G_{\text{adv}}(x,y)=\lim _{\varepsilon \to 0}{\frac {1}{(2\pi )^{4}}}\int d^{4}p\,{\frac {e^{-ip(x-y)}}{(p_{0}-i\varepsilon )^{2}-{\vec {p}}^{2}-m^{2}}}=-{\frac {\Theta (y^{0}-x^{0})}{2\pi }}\delta (\tau _{xy}^{2})+\Theta (y^{0}-x^{0})\Theta (\tau _{xy}^{2}){\frac {mJ_{1}(m\tau _{xy})}{4\pi \tau _{xy}}}.$

This expression can also be expressed in terms of the vacuum expectation value of the commutator of the free scalar field. In this case, $G_{\text{adv}}(x,y)=i\langle 0|\left[\Phi (x),\Phi (y)\right]|0\rangle \Theta (y^{0}-x^{0})~.$

#### Feynman propagator

A contour going under the left pole and over the right pole gives the **Feynman propagator**, introduced by Richard Feynman in 1948.

This choice of contour is equivalent to calculating the limit $G_{F}(x,y)=\lim _{\varepsilon \to 0}{\frac {1}{(2\pi )^{4}}}\int d^{4}p\,{\frac {e^{-ip(x-y)}}{p^{2}-m^{2}+i\varepsilon }}={\begin{cases}-{\frac {1}{4\pi }}\delta (\tau _{xy}^{2})+{\frac {m}{8\pi \tau _{xy}}}H_{1}^{(1)}(m\tau _{xy})&\tau _{xy}^{2}\geq 0\\-{\frac {im}{4\pi ^{2}{\sqrt {-\tau _{xy}^{2}}}}}K_{1}(m{\sqrt {-\tau _{xy}^{2}}})&\tau _{xy}^{2}<0.\end{cases}}$

Here, *H*1(1) is a Hankel function and *K*1 is a modified Bessel function.

This expression can be derived directly from the field theory as the vacuum expectation value of the *time-ordered product* of the free scalar field, that is, the product always taken such that the time ordering of the spacetime points is the same, ${\begin{aligned}G_{F}(x-y)&=-i\langle 0|T(\Phi (x)\Phi (y))|0\rangle \\[4pt]&=-i\left\langle 0|\left[\Theta (x^{0}-y^{0})\Phi (x)\Phi (y)+\Theta (y^{0}-x^{0})\Phi (y)\Phi (x)\right]|0\right\rangle .\end{aligned}}$

This expression is Lorentz invariant, as long as the field operators commute with one another when the points x and y are separated by a spacelike interval.

The usual derivation is to insert a complete set of single-particle momentum states between the fields with Lorentz covariant normalization, and then to show that the two Θ functions, one for the particle and one for its anti-particle, providing the causal time ordering may be obtained by a contour integral along the energy axis, if the integrand is as above (hence the infinitesimal imaginary part), to move the pole off the real line.

The propagator may also be derived using the path integral formulation of quantum theory.

#### Dirac propagator

Introduced by Paul Dirac in 1938.

### Momentum space propagator

The Fourier transform of the position space propagators can be thought of as propagators in momentum space. These take a much simpler form than the position space propagators.

They are often written with an explicit ε term although this is understood to be a reminder about which integration contour is appropriate (see above). This ε term is included to incorporate boundary conditions and causality (see below).

For a 4-momentum p the causal and Feynman propagators in momentum space are:

${\tilde {G}}_{\text{ret}}(p)={\frac {1}{(p_{0}+i\varepsilon )^{2}-{\vec {p}}^{2}-m^{2}}}$

${\tilde {G}}_{\text{adv}}(p)={\frac {1}{(p_{0}-i\varepsilon )^{2}-{\vec {p}}^{2}-m^{2}}}$

${\tilde {G}}_{F}(p)={\frac {1}{p^{2}-m^{2}+i\varepsilon }}.$

For purposes of Feynman diagram calculations, it is usually convenient to write these with an additional overall factor of i (conventions vary).

### Faster than light?

The Feynman propagator has some properties that seem baffling at first. In particular, unlike the commutator, the propagator is *nonzero* outside of the light cone, though it falls off rapidly for spacelike intervals. Interpreted as an amplitude for particle motion, this translates to the virtual particle travelling faster than light. It is not immediately obvious how this can be reconciled with causality: can we use faster-than-light virtual particles to send faster-than-light messages?

The answer is no: while in classical mechanics the intervals along which particles and causal effects can travel are the same, this is no longer true in quantum field theory, where it is commutators that determine which operators can affect one another.

So what *does* the spacelike part of the propagator represent? In QFT the vacuum is an active participant, and particle numbers and field values are related by an uncertainty principle; field values are uncertain even for particle number *zero*. There is a nonzero probability amplitude to find a significant fluctuation in the vacuum value of the field Φ(*x*) if one measures it locally (or, to be more precise, if one measures an operator obtained by averaging the field over a small region). Furthermore, the dynamics of the fields tend to favor spatially correlated fluctuations to some extent. The nonzero time-ordered product for spacelike-separated fields then just measures the amplitude for a nonlocal correlation in these vacuum fluctuations, analogous to an EPR correlation. Indeed, the propagator is often called a *two-point correlation function* for the free field.

Since, by the postulates of quantum field theory, all observable operators commute with each other at spacelike separation, messages can no more be sent through these correlations than they can through any other EPR correlations; the correlations are in random variables.

Regarding virtual particles, the propagator at spacelike separation can be thought of as a means of calculating the amplitude for creating a virtual particle-antiparticle pair that eventually disappears into the vacuum, or for detecting a virtual pair emerging from the vacuum. In Feynman's language, such creation and annihilation processes are equivalent to a virtual particle wandering backward and forward through time, which can take it outside of the light cone. However, no signaling back in time is allowed.

#### Explanation using limits

This can be made clearer by writing the propagator in the following form for a massless particle: $G_{F}^{\varepsilon }(x,y)={\frac {\varepsilon }{(x-y)^{2}+i\varepsilon ^{2}}}.$

This is the usual definition but normalised by a factor of $\varepsilon$ . Then the rule is that one only takes the limit $\varepsilon \to 0$ at the end of a calculation.

One sees that $G_{F}^{\varepsilon }(x,y)={\frac {-i}{\varepsilon }}\quad {\text{if}}~~~(x-y)^{2}=0,$ and $\lim _{\varepsilon \to 0}G_{F}^{\varepsilon }(x,y)=0\quad {\text{if}}~~~(x-y)^{2}\neq 0.$ Hence this means that a single massless particle will always stay on the light cone. It is also shown that the total probability for a photon at any time must be normalised by the reciprocal of the following factor: $\lim _{\varepsilon \to 0}\int |G_{F}^{\varepsilon }(0,x)|^{2}\,dx^{3}=\lim _{\varepsilon \to 0}\int {\frac {\varepsilon ^{2}}{(\mathbf {x} ^{2}-t^{2})^{2}+\varepsilon ^{4}}}\,dx^{3}=2\pi ^{2}|t|.$ We see that the parts outside the light cone usually are zero in the limit and only are important in Feynman diagrams.

### Propagators in Feynman diagrams

The most common use of the propagator is in calculating probability amplitudes for particle interactions using Feynman diagrams. These calculations are usually carried out in momentum space. In general, the amplitude gets a factor of the propagator for every *internal line*, that is, every line that does not represent an incoming or outgoing particle in the initial or final state. It will also get a factor proportional to, and similar in form to, an interaction term in the theory's Lagrangian for every internal vertex where lines meet. These prescriptions are known as *Feynman rules*.

Internal lines correspond to virtual particles. Since the propagator does not vanish for combinations of energy and momentum disallowed by the classical equations of motion, we say that the virtual particles are allowed to be off shell. In fact, since the propagator is obtained by inverting the wave equation, in general, it will have singularities on shell.

The energy carried by the particle in the propagator can even be *negative*. This can be interpreted simply as the case in which, instead of a particle going one way, its antiparticle is going the *other* way, and therefore carrying an opposing flow of positive energy. The propagator encompasses both possibilities. It does mean that one has to be careful about minus signs for the case of fermions, whose propagators are not even functions in the energy and momentum (see below).

Virtual particles conserve energy and momentum. However, since they can be off shell, wherever the diagram contains a closed *loop*, the energies and momenta of the virtual particles participating in the loop will be partly unconstrained, since a change in a quantity for one particle in the loop can be balanced by an equal and opposite change in another. Therefore, every loop in a Feynman diagram requires an integral over a continuum of possible energies and momenta. In general, these integrals of products of propagators can diverge, a situation that must be handled by the process of renormalization.

### Other theories

#### Spin 1⁄2

If the particle possesses spin then its propagator is in general somewhat more complicated, as it will involve the particle's spin or polarization indices. The differential equation satisfied by the propagator for a spin 1⁄2 particle is given by

$(i\not \nabla '-m)S_{F}(x',x)=I_{4}\delta ^{4}(x'-x),$

where *I*4 is the unit matrix in four dimensions, and employing the Feynman slash notation. This is the Dirac equation for a delta function source in spacetime. Using the momentum representation, $S_{F}(x',x)=\int {\frac {d^{4}p}{(2\pi )^{4}}}\exp {\left[-ip\cdot (x'-x)\right]}{\tilde {S}}_{F}(p),$ the equation becomes

${\begin{aligned}&(i\not \nabla '-m)\int {\frac {d^{4}p}{(2\pi )^{4}}}{\tilde {S}}_{F}(p)\exp {\left[-ip\cdot (x'-x)\right]}\\[6pt]={}&\int {\frac {d^{4}p}{(2\pi )^{4}}}(\not p-m){\tilde {S}}_{F}(p)\exp {\left[-ip\cdot (x'-x)\right]}\\[6pt]={}&\int {\frac {d^{4}p}{(2\pi )^{4}}}I_{4}\exp {\left[-ip\cdot (x'-x)\right]}\\[6pt]={}&I_{4}\delta ^{4}(x'-x),\end{aligned}}$

where on the right-hand side an integral representation of the four-dimensional delta function is used. Thus

$(\not p-mI_{4}){\tilde {S}}_{F}(p)=I_{4}.$

By multiplying from the left with $(\not p+m)$ (dropping unit matrices from the notation) and using properties of the gamma matrices, ${\begin{aligned}\not p\not p&={\tfrac {1}{2}}(\not p\not p+\not p\not p)\\[6pt]&={\tfrac {1}{2}}(\gamma _{\mu }p^{\mu }\gamma _{\nu }p^{\nu }+\gamma _{\nu }p^{\nu }\gamma _{\mu }p^{\mu })\\[6pt]&={\tfrac {1}{2}}(\gamma _{\mu }\gamma _{\nu }+\gamma _{\nu }\gamma _{\mu })p^{\mu }p^{\nu }\\[6pt]&=g_{\mu \nu }p^{\mu }p^{\nu }=p_{\nu }p^{\nu }=p^{2},\end{aligned}}$

the momentum-space propagator used in Feynman diagrams for a Dirac field representing the electron in quantum electrodynamics is found to have form

${\tilde {S}}_{F}(p)={\frac {(\not p+m)}{p^{2}-m^{2}+i\varepsilon }}={\frac {(\gamma ^{\mu }p_{\mu }+m)}{p^{2}-m^{2}+i\varepsilon }}.$

The *iε* downstairs is a prescription for how to handle the poles in the complex *p*0-plane. It automatically yields the Feynman contour of integration by shifting the poles appropriately. It is sometimes written

${\tilde {S}}_{F}(p)={1 \over \gamma ^{\mu }p_{\mu }-m+i\varepsilon }={1 \over \not p-m+i\varepsilon }$

for short. It should be remembered that this expression is just shorthand notation for (*γ**μ**p**μ* − *m*)−1. "One over matrix" is otherwise nonsensical. In position space one has $S_{F}(x-y)=\int {\frac {d^{4}p}{(2\pi )^{4}}}\,e^{-ip\cdot (x-y)}{\frac {\gamma ^{\mu }p_{\mu }+m}{p^{2}-m^{2}+i\varepsilon }}=\left({\frac {\gamma ^{\mu }(x-y)_{\mu }}{|x-y|^{5}}}+{\frac {m}{|x-y|^{3}}}\right)J_{1}(m|x-y|).$

This is related to the Feynman propagator by

$S_{F}(x-y)=(i\not \partial +m)G_{F}(x-y)$

where $\not \partial :=\gamma ^{\mu }\partial _{\mu }$ .

#### Spin 1

The propagator for a gauge boson in a gauge theory depends on the choice of convention to fix the gauge. For the gauge used by Feynman and Stueckelberg, the propagator for a photon is

${-ig^{\mu \nu } \over p^{2}+i\varepsilon }.$

The general form with gauge parameter *λ*, up to overall sign and the factor of i , reads

$-i{\frac {g^{\mu \nu }+\left(1-{\frac {1}{\lambda }}\right){\frac {p^{\mu }p^{\nu }}{p^{2}}}}{p^{2}+i\varepsilon }}.$

The propagator for a massive vector field can be derived from the Stueckelberg Lagrangian. The general form with gauge parameter *λ*, up to overall sign and the factor of i , reads

${\frac {g_{\mu \nu }-{\frac {k_{\mu }k_{\nu }}{m^{2}}}}{k^{2}-m^{2}+i\varepsilon }}+{\frac {\frac {k_{\mu }k_{\nu }}{m^{2}}}{k^{2}-{\frac {m^{2}}{\lambda }}+i\varepsilon }}.$

With these general forms one obtains the propagators in unitary gauge for *λ* = 0, the propagator in Feynman or 't Hooft gauge for *λ* = 1 and in Landau or Lorenz gauge for *λ* = ∞. There are also other notations where the gauge parameter is the inverse of λ, usually denoted ξ (see *R*ξ gauges). The name of the propagator, however, refers to its final form and not necessarily to the value of the gauge parameter.

Unitary gauge:

${\frac {g_{\mu \nu }-{\frac {k_{\mu }k_{\nu }}{m^{2}}}}{k^{2}-m^{2}+i\varepsilon }}.$

Feynman ('t Hooft) gauge:

${\frac {g_{\mu \nu }}{k^{2}-m^{2}+i\varepsilon }}.$

Landau (Lorenz) gauge:

${\frac {g_{\mu \nu }-{\frac {k_{\mu }k_{\nu }}{k^{2}}}}{k^{2}-m^{2}+i\varepsilon }}.$

### Graviton propagator

The graviton propagator for Minkowski space in general relativity is $G_{\alpha \beta ~\mu \nu }={\frac {{\mathcal {P}}_{\alpha \beta ~\mu \nu }^{2}}{k^{2}}}-{\frac {{\mathcal {P}}_{s}^{0}{}_{\alpha \beta ~\mu \nu }}{2k^{2}}}={\frac {g_{\alpha \mu }g_{\beta \nu }+g_{\beta \mu }g_{\alpha \nu }-{\frac {2}{D-2}}g_{\mu \nu }g_{\alpha \beta }}{k^{2}}},$ where D is the number of spacetime dimensions, ${\mathcal {P}}^{2}$ is the transverse and traceless spin-2 projection operator and ${\mathcal {P}}_{s}^{0}$ is a spin-0 scalar multiplet. The graviton propagator for (Anti) de Sitter space is $G={\frac {{\mathcal {P}}^{2}}{2H^{2}-\Box }}+{\frac {{\mathcal {P}}_{s}^{0}}{2(\Box +4H^{2})}},$ where H is the Hubble constant. Note that upon taking the limit $H\to 0$ and $\Box \to -k^{2}$ , the AdS propagator reduces to the Minkowski propagator.

The scalar propagators are Green's functions for the Klein–Gordon equation. There are related singular functions which are important in quantum field theory. These functions are most simply defined in terms of the vacuum expectation value of products of field operators.

### Solutions to the Klein–Gordon equation

#### Pauli–Jordan function (also called *the* causal propagator)

The commutator of two scalar field operators defines the Pauli–Jordan function $\Delta (x-y)$ by

$\langle 0|\left[\Phi (x),\Phi (y)\right]|0\rangle =i\,\Delta (x-y)$

with

$\,\Delta (x-y)=G_{\text{ret}}(x-y)-G_{\text{adv}}(x-y)$

This satisfies

$\Delta (x-y)=-\Delta (y-x)$

and is zero if $(x-y)^{2}<0$ .

#### Positive and negative frequency parts (cut propagators)

We can define the positive and negative frequency parts of $\Delta (x-y)$ , sometimes called cut propagators, in a relativistically invariant way.

This allows us to define the positive frequency part:

$\Delta _{+}(x-y)=\langle 0|\Phi (x)\Phi (y)|0\rangle ,$

and the negative frequency part:

$\Delta _{-}(x-y)=\langle 0|\Phi (y)\Phi (x)|0\rangle .$

These satisfy

$\,i\Delta =\Delta _{+}-\Delta _{-}$

and

$(\Box _{x}+m^{2})\Delta _{\pm }(x-y)=0.$

#### Auxiliary function

The anti-commutator of two scalar field operators defines $\Delta _{1}(x-y)$ function by

$\langle 0|\left\{\Phi (x),\Phi (y)\right\}|0\rangle =\Delta _{1}(x-y)$

with

$\,\Delta _{1}(x-y)=\Delta _{+}(x-y)+\Delta _{-}(x-y).$

This satisfies $\,\Delta _{1}(x-y)=\Delta _{1}(y-x).$

### Green's functions for the Klein–Gordon equation

The retarded, advanced and Feynman propagators defined above are all Green's functions for the Klein–Gordon equation.

They are related to the singular functions by

$G_{\text{ret}}(x-y)=\Delta (x-y)\Theta (x^{0}-y^{0})$

$G_{\text{adv}}(x-y)=-\Delta (x-y)\Theta (y^{0}-x^{0})$

$2G_{F}(x-y)=-i\,\Delta _{1}(x-y)+\varepsilon (x^{0}-y^{0})\,\Delta (x-y)$

where $\varepsilon (x^{0}-y^{0})$ is the sign of $x^{0}-y^{0}$ .
