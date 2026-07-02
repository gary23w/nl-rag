---
title: "Van der Pol oscillator"
source: https://en.wikipedia.org/wiki/Van_der_Pol_oscillator
domain: singular-perturbation
license: CC-BY-SA-4.0
tags: singular perturbation, boundary layer, matched asymptotic expansions, relaxation oscillator
fetched: 2026-07-02
---

# Van der Pol oscillator

In the study of dynamical systems, the **van der Pol oscillator** (named for Dutch physicist Balthasar van der Pol) is a non-conservative, oscillating system with non-linear damping. It evolves in time according to the second-order differential equation ${d^{2}x \over dt^{2}}=\mu (1-x^{2}){dx \over dt}-x,$ where x is the position coordinate—which is a function of the time t—and μ is a scalar parameter indicating the nonlinearity and the strength of the damping.

## History

The Van der Pol oscillator was originally proposed by the Dutch electrical engineer and physicist Balthasar van der Pol while he was working at Philips. Van der Pol found stable oscillations, which he subsequently called relaxation-oscillations and are now known as a type of limit cycle, in electrical circuits employing vacuum tubes. When these circuits are driven near the limit cycle, they become entrained, i.e. the driving signal pulls the current along with it. Van der Pol and his colleague, van der Mark, reported in the September 1927 issue of *Nature* that at certain drive frequencies an irregular noise was heard, which was later found to be the result of deterministic chaos.

The Van der Pol equation has a long history of being used in both the physical and biological sciences. For instance, in biology, Fitzhugh and Nagumo extended the equation in a planar field as a model for action potentials of neurons. The equation has also been utilised in seismology to model the two plates in a geological fault, and in studies of phonation to model the right and left vocal fold oscillators.

## Two-dimensional form

Liénard's theorem can be used to prove that the system has a limit cycle. Applying the Liénard transformation $y=x-x^{3}/3-{\dot {x}}/\mu$ , where the dot indicates the time derivative, the Van der Pol oscillator can be written in its two-dimensional form:

${\dot {x}}=\mu \left(x-{\tfrac {1}{3}}x^{3}-y\right)$

${\dot {y}}={\frac {1}{\mu }}x$

.

Another commonly used form based on the transformation $y={\dot {x}}$ leads to:

${\dot {x}}=y$

${\dot {y}}=\mu (1-x^{2})y-x$

.

## Results for the unforced oscillator

- When *μ* = 0, i.e. there is no damping function, the equation becomes ${\frac {d^{2}x}{dt^{2}}}+x=0.$ This is a form of the simple harmonic oscillator, and there is always conservation of energy.

- When *μ* > 0, all initial conditions converge to a globally unique limit cycle. Near the origin $x={\tfrac {dx}{dt}}=0,$ the system is unstable, and far from the origin, the system is damped.
- The Van der Pol oscillator does not have an exact, analytic solution. However, such a solution does exist for the limit cycle if *f*(*x*) in the Lienard equation is a constant piece-wise function.
- The period at small μ has serial expansion $T={\frac {2\pi }{1-\mu ^{2}/16+17\mu ^{4}/3072+O(\mu ^{6})}}.$ See Poincaré–Lindstedt method for a derivation to order 2. See chapter 10 of for a derivation up to order 3, and for a numerical derivation up to order 164.
- For large μ, the behavior of the oscillator has a slow buildup, fast release cycle (a cycle of building up the tension and releasing the tension, thus a **relaxation oscillation**). This is most easily seen in the form ${\dot {x}}=\mu \left(x-{\frac {1}{3}}x^{3}-y\right)\!,\quad {\dot {y}}={\frac {1}{\mu }}x.$ In this form, the oscillator completes one cycle as follows:
  - Slowly ascending the right branch of the cubic curve $y=x-{\tfrac {x^{3}}{3}},$ from (2, –2/3) to (1, 2/3).
  - Rapidly moving to the left branch of the cubic curve, from (1, 2/3) to (–2, 2/3).
  - Repeat the two steps on the left branch.
- The leading term in the period of the cycle is due to the slow ascending and descending, which can be computed as: $T=2\int dt=2\int \mu {\frac {dy}{x}}=2\mu \int _{2}^{1}{\frac {dy}{dx}}{\frac {dx}{x}}=(3-2\ln 2)\mu$ Higher orders of the period of the cycle is $T=(3-2\ln 2)\mu +3\alpha \mu ^{-1/3}-{\frac {22}{9\mu }}\ln \mu +{\frac {0.0087\cdots }{\mu }}+O(\mu ^{-4/3}).$ where *α* ≈ 2.338 is the smallest root of Ai(–*α*) = 0, where Ai is the Airy function. (Section 9.7 ) ( contains a derivation, but has a misprint of 3*α* to 2*α*.) This was derived by Anatoly Dorodnitsyn.
- The amplitude of the cycle is $2+{\frac {\alpha }{3}}\mu ^{-4/3}-{\frac {16}{27}}\mu ^{-2}\ln \mu +O(\mu ^{-2})$

## Hopf bifurcation

As μ moves from less than zero to more than zero, the spiral sink at origin becomes a spiral source, and a limit cycle appears "out of the blue" with radius two. This is because the transition is not generic: when *ε* = 0, both the differential equation becomes linear, and the origin becomes a circular node.

Knowing that in a Hopf bifurcation, the limit cycle should have size $\propto \varepsilon ^{1/2},$ we may attempt to convert this to a Hopf bifurcation by using the change of variables $u=\varepsilon ^{1/2}x,$ which gives ${\ddot {u}}+u+u^{2}{\dot {u}}-\varepsilon {\dot {u}}=0$ This indeed is a Hopf bifurcation.

## Hamiltonian for Van der Pol oscillator

One can also write a time-independent Hamiltonian formalism for the Van der Pol oscillator by augmenting it to a four-dimensional autonomous dynamical system using an auxiliary second-order nonlinear differential equation as follows:

${\ddot {x}}-\mu (1-x^{2}){\dot {x}}+x=0,$

${\ddot {y}}+\mu (1-x^{2}){\dot {y}}+y=0.$

Note that the dynamics of the original Van der Pol oscillator is not affected due to the one-way coupling between the time-evolutions of *x* and *y* variables. A Hamiltonian *H* for this system of equations can be shown to be

$H(x,y,p_{x},p_{y})=p_{x}p_{y}+xy-\mu (1-x^{2})yp_{y},$

where $p_{x}={\dot {y}}+\mu (1-x^{2})y$ and $p_{y}={\dot {x}}$ are the conjugate momenta corresponding to *x* and *y*, respectively. This may, in principle, lead to quantization of the Van der Pol oscillator. Such a Hamiltonian also connects the geometric phase of the limit cycle system having time dependent parameters with the Hannay angle of the corresponding Hamiltonian system.

### Quantum oscillator

The quantum van der Pol oscillator, which is the quantum mechanical version of the classical van der Pol oscillator, has been proposed using a Lindblad equation to study its quantum dynamics and quantum synchronization. Note the above Hamiltonian approach with an auxiliary second-order equation produces unbounded phase-space trajectories and hence cannot be used to quantize the van der Pol oscillator. In the limit of weak nonlinearity (i.e. *μ→*0) the van der Pol oscillator reduces to the Stuart–Landau equation. The Stuart–Landau equation in fact describes an entire class of limit-cycle oscillators in the weakly-nonlinear limit. The form of the classical Stuart–Landau equation is much simpler, and perhaps not surprisingly, can be quantized by a Lindblad equation which is also simpler than the Lindblad equation for the van der Pol oscillator. The quantum Stuart–Landau model has played an important role in the study of quantum synchronisation (where it has often been called a van der Pol oscillator although it cannot be uniquely associated with the van der Pol oscillator). The relationship between the classical Stuart–Landau model (*μ→*0) and more general limit-cycle oscillators (arbitrary *μ*) has also been demonstrated numerically in the corresponding quantum models.

## Forced Van der Pol oscillator

The forced, or driven, Van der Pol oscillator takes the 'original' function and adds a driving function *A*sin(*ωt*) to give a differential equation of the form:

${d^{2}x \over dt^{2}}-\mu (1-x^{2}){dx \over dt}+x-A\sin(\omega t)=0,$

where A is the amplitude, or displacement, of the wave function and ω is its angular velocity.

## Popular culture

Author James Gleick described a vacuum tube Van der Pol oscillator in his book from 1987 *Chaos: Making a New Science*. According to a *New York Times* article, Gleick received a modern electronic Van der Pol oscillator from a reader in 1988.
