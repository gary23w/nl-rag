---
title: "Stochastic differential equation"
source: https://en.wikipedia.org/wiki/Stochastic_differential_equation
domain: stochastic-calculus
license: CC-BY-SA-4.0
tags: stochastic calculus, stochastic differential equation, wiener process, feynman-kac formula
fetched: 2026-07-02
---

# Stochastic differential equation

A **stochastic differential equation** (**SDE**) is a differential equation in which one or more of the terms is a stochastic process, resulting in a solution which is also a stochastic process. SDEs have many applications throughout pure mathematics and are used to model various behaviours of stochastic models such as prices of listed company shares, random growth models or physical systems that are subjected to thermal fluctuations.

SDEs have a random differential that is in the most basic case random white noise calculated as the distributional derivative of a Brownian motion or more generally a semimartingale. However, other types of random behaviour are possible, such as jump processes like Lévy processes or semimartingales with jumps.

Stochastic differential equations are in general neither differential equations nor random differential equations. Random differential equations are conjugate to stochastic differential equations. Stochastic differential equations can also be extended to differential manifolds.

## Background

Stochastic differential equations originated in the theory of Brownian motion, in the work of Albert Einstein and Marian Smoluchowski in 1905, although Louis Bachelier was the first person credited with modeling Brownian motion in 1900, giving a very early example of a stochastic differential equation now known as Bachelier model. Some of these early examples were linear stochastic differential equations, also called Langevin equations after French physicist Langevin, describing the motion of a harmonic oscillator subject to a random force. The mathematical theory of stochastic differential equations was developed in the 1940s through the groundbreaking work of Japanese mathematician Kiyosi Itô, who introduced the concept of stochastic integral and initiated the study of nonlinear stochastic differential equations. Another approach was later proposed by Russian physicist Stratonovich, leading to a calculus similar to ordinary calculus.

### Terminology

The most common form of SDEs in the literature is an ordinary differential equation with the right hand side perturbed by a term dependent on a white noise variable. In most cases, SDEs are understood as continuous time limit of the corresponding stochastic difference equations. This understanding of SDEs is ambiguous and must be complemented by a proper mathematical definition of the corresponding integral. Such a mathematical definition was first proposed by Kiyosi Itô in the 1940s, leading to what is known today as the Itô calculus. Another construction was later proposed by Russian physicist Stratonovich, leading to what is known as the Stratonovich integral. The Itô integral and Stratonovich integral are related, but different, objects and the choice between them depends on the application considered. The Itô calculus is based on the concept of non-anticipativeness or causality, which is natural in applications where the variable is time. The Stratonovich calculus, on the other hand, has rules which resemble ordinary calculus and has intrinsic geometric properties which render it more natural when dealing with geometric problems such as random motion on manifolds, although it is possible and in some cases preferable to model random motion on manifolds through Itô SDEs, for example when trying to optimally approximate SDEs on submanifolds.

An alternative view on SDEs is the stochastic flow of diffeomorphisms. This understanding is unambiguous and corresponds to the Stratonovich version of the continuous time limit of stochastic difference equations. Associated with SDEs is the Smoluchowski equation or the Fokker–Planck equation, an equation describing the time evolution of probability distribution functions. The generalization of the Fokker–Planck evolution to temporal evolution of differential forms is provided by the concept of stochastic evolution operator.

In physical science, there is an ambiguity in the usage of the term "Langevin SDEs". While Langevin SDEs can be of a more general form, this term typically refers to a narrow class of SDEs with gradient flow vector fields. This class of SDEs is particularly popular because it is a starting point of the Parisi–Sourlas stochastic quantization procedure, leading to a N=2 supersymmetric model closely related to supersymmetric quantum mechanics. From the physical point of view, however, this class of SDEs is not very interesting because it never exhibits spontaneous breakdown of topological supersymmetry, i.e., (overdamped) Langevin SDEs are never chaotic.

### Stochastic calculus

Brownian motion or the Wiener process was discovered to be exceptionally complex mathematically. The Wiener process is almost surely nowhere differentiable; thus, it requires its own rules of calculus. There are two dominating versions of stochastic calculus, the Itô stochastic calculus and the Stratonovich stochastic calculus. Each of the two has advantages and disadvantages, and newcomers are often confused whether the one is more appropriate than the other in a given situation. Guidelines exist (e.g. Øksendal, 2003) and conveniently, one can readily convert an Itô SDE to an equivalent Stratonovich SDE and back again. Still, one must be careful which calculus to use when the SDE is initially written down.

### Numerical solutions

Numerical methods for solving stochastic differential equations include the Euler–Maruyama method, Milstein method, Runge–Kutta method (SDE), Rosenbrock method, and methods based on different representations of iterated stochastic integrals.

## Use in physics

In physics, SDEs have wide applicability ranging from molecular dynamics to neurodynamics and to the dynamics of astrophysical objects. More specifically, SDEs describe all dynamical systems, in which quantum effects are either unimportant or can be taken into account as perturbations. SDEs can be viewed as a generalization of the dynamical systems theory to models with noise. This is an important generalization because real systems cannot be completely isolated from their environments and for this reason always experience external stochastic influence.

There are standard techniques for transforming higher-order equations into several coupled first-order equations by introducing new unknowns. Therefore, the following is the most general class of SDEs:

${\frac {\mathrm {d} x(t)}{\mathrm {d} t}}=F(x(t))+\sum _{\alpha =1}^{n}g_{\alpha }(x(t))\xi ^{\alpha }(t),\,$

where $x\in X$ is the position in the system in its phase (or state) space, X , assumed to be a differentiable manifold, the $F\in TX$ is a flow vector field representing deterministic law of evolution, and $g_{\alpha }\in TX$ is a set of vector fields that define the coupling of the system to Gaussian white noise, $\xi ^{\alpha }$ . If X is a linear space and g are constants, the system is said to be subject to additive noise, otherwise it is said to be subject to multiplicative noise. For additive noise, the Itô and Stratonovich forms of the SDE generate the same solution, and it is not important which definition is used to solve the SDE. For multiplicative noise SDEs the Itô and Stratonovich forms of the SDE are different, and care should be used in mapping between them.

For a fixed configuration of noise, SDE has a unique solution differentiable with respect to the initial condition. Nontriviality of stochastic case shows up when one tries to average various objects of interest over noise configurations. In this sense, an SDE is not a uniquely defined entity when noise is multiplicative and when the SDE is understood as a continuous time limit of a stochastic difference equation. In this case, SDE must be complemented by what is known as "interpretations of SDE" such as Itô or a Stratonovich interpretations of SDEs. Nevertheless, when SDE is viewed as a continuous-time stochastic flow of diffeomorphisms, it is a uniquely defined mathematical object that corresponds to Stratonovich approach to a continuous time limit of a stochastic difference equation.

In physics, the main method of solution is to find the probability distribution function as a function of time using the equivalent Fokker–Planck equation (FPE). The Fokker–Planck equation is a deterministic partial differential equation. It tells how the probability distribution function evolves in time similarly to how the Schrödinger equation gives the time evolution of the quantum wave function or the diffusion equation gives the time evolution of chemical concentration. Alternatively, numerical solutions can be obtained by Monte Carlo simulation. Other techniques include the path integration that draws on the analogy between statistical physics and quantum mechanics (for example, the Fokker-Planck equation can be transformed into the Schrödinger equation by rescaling a few variables) or by writing down ordinary differential equations for the statistical moments of the probability distribution function.

## Use in probability and mathematical finance

The notation used in probability theory (and in many applications of probability theory, for instance in signal processing with the filtering problem and in mathematical finance) is slightly different. It is also the notation used in publications on numerical methods for solving stochastic differential equations. This notation makes the exotic nature of the random function of time $\xi ^{\alpha }$ in the physics formulation more explicit. In strict mathematical terms, $\xi ^{\alpha }$ cannot be chosen as an ordinary function, but only as a generalized function. The mathematical formulation treats this complication with less ambiguity than the physics formulation.

A typical equation is of the form

$\mathrm {d} X_{t}=\mu (X_{t},t)\,\mathrm {d} t+\sigma (X_{t},t)\,\mathrm {d} B_{t},$

where B denotes a Wiener process (standard Brownian motion). This equation should be interpreted as an informal way of expressing the corresponding integral equation

$X_{t+s}-X_{t}=\int _{t}^{t+s}\mu (X_{u},u)\mathrm {d} u+\int _{t}^{t+s}\sigma (X_{u},u)\,\mathrm {d} B_{u}.$

The equation above characterizes the behavior of the continuous time stochastic process *X**t* as the sum of an ordinary Lebesgue integral and an Itô integral. A heuristic (but very helpful) interpretation of the stochastic differential equation is that in a small time interval of length *δ* the stochastic process *X**t* changes its value by an amount that is normally distributed with expectation *μ*(*X**t*, *t*) *δ* and variance *σ*(*X**t*, *t*)2 *δ* and is independent of the past behavior of the process. This is so because the increments of a Wiener process are independent and normally distributed. The function *μ* is referred to as the drift coefficient, while *σ* is called the diffusion coefficient. The stochastic process *X**t* is called a diffusion process, and satisfies the Markov property.

The formal interpretation of an SDE is given in terms of what constitutes a solution to the SDE. There are two main definitions of a solution to an SDE, a strong solution and a weak solution Both require the existence of a process *X**t* that solves the integral equation version of the SDE. The difference between the two lies in the underlying probability space ( $\Omega ,\,{\mathcal {F}},\,P$ ). A weak solution consists of a probability space and a process that satisfies the integral equation, while a strong solution is a process that satisfies the equation and is defined on a given probability space. The Yamada–Watanabe theorem makes a connection between the two.

An important example is the equation for geometric Brownian motion

$\mathrm {d} X_{t}=\mu X_{t}\,\mathrm {d} t+\sigma X_{t}\,\mathrm {d} B_{t}.$

which is the equation for the dynamics of the price of a listed company share in the Black–Scholes options pricing model of financial mathematics.

Generalizing the geometric Brownian motion, it is also possible to define SDEs admitting strong solutions and whose distribution is a convex combination of densities coming from different geometric Brownian motions or Black Scholes models, obtaining a single SDE whose solutions is distributed as a mixture dynamics of lognormal distributions of different Black Scholes models. This leads to models that can deal with the volatility smile in financial mathematics.

The simpler SDE called arithmetic Brownian motion

$\mathrm {d} X_{t}=\mu \,\mathrm {d} t+\sigma \,\mathrm {d} B_{t}$

was used by Louis Bachelier as the first model for stock prices in 1900, known today as Bachelier model.

There are also more general stochastic differential equations where the coefficients *μ* and *σ* depend not only on the present value of the process *X**t*, but also on previous values of the process and possibly on present or previous values of other processes too. In that case the solution process, *X*, is not a Markov process, and it is called an Itô process and not a diffusion process. When the coefficients depends only on present and past values of *X*, the defining equation is called a stochastic delay differential equation.

A generalization of stochastic differential equations with the Fisk-Stratonovich integral to semimartingales with jumps are the SDEs of *Marcus type*. The Marcus integral is an extension of McShane's stochastic calculus.

An application in stochastic finance derives from the usage of the equation for Ornstein–Uhlenbeck process

$\mathrm {d} R_{t}=\mu R_{t}\,\mathrm {d} t+\sigma _{t}\,\mathrm {d} B_{t}.$

which is the equation for the dynamics of the return of the price of a listed company share under the hypothesis that returns display a Log-normal distribution. Under this hypothesis, the methodologies developed by Marcello Minenna determines prediction interval able to identify abnormal return that could hide market abuse phenomena.

### SDEs on manifolds

More generally one can extend the theory of stochastic calculus onto differential manifolds and for this purpose one uses the Fisk-Stratonovich integral. Consider a manifold M , some finite-dimensional vector space E , a filtered probability space $(\Omega ,{\mathcal {F}},({\mathcal {F}}_{t})_{t\in \mathbb {R} _{+}},P)$ with $({\mathcal {F}}_{t})_{t\in \mathbb {R} _{+}}$ satisfying the usual conditions and let ${\widehat {M}}=M\cup \{\infty \}$ be the one-point compactification and $x_{0}$ be ${\mathcal {F}}_{0}$ -measurable. A *stochastic differential equation on M* written

$\mathrm {d} X=A(X)\circ dZ$

is a pair $(A,Z)$ , such that

- Z is a continuous E -valued semimartingale,
- $A:M\times E\to TM,(x,e)\mapsto A(x)e$ is a homomorphism of vector bundles over M .

For each $x\in M$ the map $A(x):E\to T_{x}M$ is linear and $A(\cdot )e\in \Gamma (TM)$ for each $e\in E$ .

A solution to the SDE on M with initial condition $X_{0}=x_{0}$ is a continuous $\{{\mathcal {F}}_{t}\}$ -adapted M -valued process $(X_{t})_{t<\zeta }$ up to life time $\zeta$ , s.t. for each test function $f\in C_{c}^{\infty }(M)$ the process $f(X)$ is a real-valued semimartingale and for each stopping time $\tau$ with $0\leq \tau <\zeta$ the equation

$f(X_{\tau })=f(x_{0})+\int _{0}^{\tau }(\mathrm {d} f)_{X}A(X)\circ \mathrm {d} Z$

holds P -almost surely, where $(df)_{X}:T_{x}M\to T_{f(x)}M$ is the differential at X . It is a *maximal solution* if the life time is maximal, i.e.,

$\{\zeta <\infty \}\subset \left\{\lim \limits _{t\nearrow \zeta }X_{t}=\infty {\text{ in }}{\widehat {M}}\right\}$

P -almost surely. It follows from the fact that $f(X)$ for each test function $f\in C_{c}^{\infty }(M)$ is a semimartingale, that X is a *semimartingale on M*. Given a maximal solution we can extend the time of X onto full $\mathbb {R} _{+}$ and after a continuation of f on ${\widehat {M}}$ we get

$f(X_{t})=f(X_{0})+\int _{0}^{t}(\mathrm {d} f)_{X}A(X)\circ \mathrm {d} Z,\quad t\geq 0$

up to indistinguishable processes. Although Stratonovich SDEs are the natural choice for SDEs on manifolds, given that they satisfy the chain rule and that their drift and diffusion coefficients behave as vector fields under changes of coordinates, there are cases where Ito calculus on manifolds is preferable. A theory of Ito calculus on manifolds was first developed by Laurent Schwartz through the concept of Schwartz morphism, see also the related 2-jet interpretation of Ito SDEs on manifolds based on the jet-bundle. This interpretation is helpful when trying to optimally approximate the solution of an SDE given on a large space with the solutions of an SDE given on a submanifold of that space, in that a Stratonovich based projection does not result to be optimal. This has been applied to the filtering problem, leading to optimal projection filters.

## As rough paths

Usually the solution of an SDE requires a probabilistic setting, as the integral implicit in the solution is a stochastic integral. If it were possible to deal with the differential equation path by path, one would not need to define a stochastic integral and one could develop a theory independently of probability theory. This points to considering the SDE

$\mathrm {d} X_{t}(\omega )=\mu (X_{t}(\omega ),t)\,\mathrm {d} t+\sigma (X_{t}(\omega ),t)\,\mathrm {d} B_{t}(\omega )$

as a single deterministic differential equation for every $\omega \in \Omega$ , where $\Omega$ is the sample space in the given probability space ( $\Omega ,\,{\mathcal {F}},\,P$ ). However, a direct path-wise interpretation of the SDE is not possible, as the Brownian motion paths have unbounded variation and are nowhere differentiable with probability one, so that there is no naive way to give meaning to terms like $\mathrm {d} B_{t}(\omega )$ , precluding also a naive path-wise definition of the stochastic integral as an integral against every single $\mathrm {d} B_{t}(\omega )$ . However, motivated by the Wong-Zakai result for limits of solutions of SDEs with regular noise and using rough paths theory, while adding a chosen definition of iterated integrals of Brownian motion, it is possible to define a deterministic rough integral for every single $\omega \in \Omega$ that coincides for example with the Ito integral with probability one for a particular choice of the iterated Brownian integral. Other definitions of the iterated integral lead to deterministic pathwise equivalents of different stochastic integrals, like the Stratonovich integral. This has been used for example in financial mathematics to price options without probability.

## Existence and uniqueness of solutions

As with deterministic ordinary and partial differential equations, it is important to know whether a given SDE has a solution, and whether or not it is unique. The following is a typical existence and uniqueness theorem for Itô SDEs taking values in *n*-dimensional Euclidean space **R***n* and driven by an *m*-dimensional Brownian motion *B*; the proof may be found in Øksendal (2003, §5.2).

Let *T* > 0, and let

$\mu :\mathbb {R} ^{n}\times [0,T]\to \mathbb {R} ^{n};$

$\sigma :\mathbb {R} ^{n}\times [0,T]\to \mathbb {R} ^{n\times m};$

be measurable functions for which there exist constants *C* and *D* such that

${\big |}\mu (x,t){\big |}+{\big |}\sigma (x,t){\big |}\leq C{\big (}1+|x|{\big )};$

${\big |}\mu (x,t)-\mu (y,t){\big |}+{\big |}\sigma (x,t)-\sigma (y,t){\big |}\leq D|x-y|;$

for all *t* ∈ [0, *T*] and all *x* and *y* ∈ **R***n*, where

$|\sigma |^{2}=\sum _{i,j=1}^{n}|\sigma _{ij}|^{2}.$

Let *Z* be a random variable that is independent of the *σ*-algebra generated by *B**s*, *s* ≥ 0, and with finite second moment:

$\mathbb {E} {\big [}|Z|^{2}{\big ]}<+\infty .$

Then the stochastic differential equation/initial value problem

$\mathrm {d} X_{t}=\mu (X_{t},t)\,\mathrm {d} t+\sigma (X_{t},t)\,\mathrm {d} B_{t}{\mbox{ for }}t\in [0,T];$

$X_{0}=Z;$

has a P-almost surely unique *t*-continuous solution (*t*, *ω*) ↦ *X**t*(*ω*) such that *X* is adapted to the filtration *F**t**Z* generated by *Z* and *B**s*, *s* ≤ *t*, and

$\mathbb {E} \left[\int _{0}^{T}|X_{t}|^{2}\,\mathrm {d} t\right]<+\infty .$

### General case: local Lipschitz condition and maximal solutions

The stochastic differential equation above is only a special case of a more general form

$\mathrm {d} Y_{t}=\alpha (t,Y_{t})\mathrm {d} X_{t}$

where

- X is a continuous semimartingale in $\mathbb {R} ^{n}$ and Y is a continuous semimartingale in $\mathbb {R} ^{d}$
- $\alpha :\mathbb {R} _{+}\times U\to \operatorname {Lin} (\mathbb {R} ^{n};\mathbb {R} ^{d})$ is a map from some open nonempty set $U\subset \mathbb {R} ^{d}$ , where $\operatorname {Lin} (\mathbb {R} ^{n};\mathbb {R} ^{d})$ is the space of all linear maps from $\mathbb {R} ^{n}$ to $\mathbb {R} ^{d}$ .

More generally one can also look at stochastic differential equations on manifolds.

Whether the solution of this equation explodes depends on the choice of $\alpha$ . Suppose $\alpha$ satisfies some local Lipschitz condition, i.e., for $t\geq 0$ and some compact set $K\subset U$ and some constant $L(t,K)$ the condition

$|\alpha (s,y)-\alpha (s,x)|\leq L(t,K)|y-x|,\quad x,y\in K,\;0\leq s\leq t,$

where $|\cdot |$ is the Euclidean norm. This condition guarantees the existence and uniqueness of a so-called *maximal solution*.

Suppose $\alpha$ is continuous and satisfies the above local Lipschitz condition and let $F:\Omega \to U$ be some initial condition, meaning it is a measurable function with respect to the initial σ-algebra. Let $\zeta :\Omega \to {\overline {\mathbb {R} }}_{+}$ be a predictable stopping time with $\zeta >0$ almost surely. A U -valued semimartingale $(Y_{t})_{t<\zeta }$ is called a *maximal solution* of

$dY_{t}=\alpha (t,Y_{t})dX_{t},\quad Y_{0}=F$

with *life time* $\zeta$ if

- for one (and hence all) announcing $\zeta _{n}\nearrow \zeta$ the stopped process $Y^{\zeta _{n}}$ is a solution to the *stopped stochastic differential equation*

$\mathrm {d} Y=\alpha (t,Y)\mathrm {d} X^{\zeta _{n}}$

- on the set $\{\zeta <\infty \}$ we have almost surely that $Y_{t}\to \partial U$ with $t\to \zeta$ .

$\zeta$ is also a so-called *explosion time*.

## Some explicitly solvable examples

Explicitly solvable SDEs include:

### Linear SDE: General case

$\mathrm {d} X_{t}=(a(t)X_{t}+c(t))\mathrm {d} t+(b(t)X_{t}+d(t))\mathrm {d} W_{t}$

$X_{t}=\Phi _{t,t_{0}}\left(X_{t_{0}}+\int _{t_{0}}^{t}\Phi _{s,t_{0}}^{-1}(c(s)-b(s)d(s))\mathrm {d} s+\int _{t_{0}}^{t}\Phi _{s,t_{0}}^{-1}d(s)\mathrm {d} W_{s}\right)$

where

$\Phi _{t,t_{0}}=\exp \left(\int _{t_{0}}^{t}\left(a(s)-{\frac {b^{2}(s)}{2}}\right)\mathrm {d} s+\int _{t_{0}}^{t}b(s)\mathrm {d} W_{s}\right)$

### Reducible SDEs: Case 1

$\mathrm {d} X_{t}={\frac {1}{2}}f(X_{t})f'(X_{t})\mathrm {d} t+f(X_{t})\mathrm {d} W_{t}$

for a given differentiable function f is equivalent to the Stratonovich SDE

$\mathrm {d} X_{t}=f(X_{t})\circ W_{t}$

which has a general solution

$X_{t}=h^{-1}(W_{t}+h(X_{0}))$

where

$h(x)=\int ^{x}{\frac {\mathrm {d} s}{f(s)}}$

### Reducible SDEs: Case 2

$\mathrm {d} X_{t}=\left(\alpha f(X_{t})+{\frac {1}{2}}f(X_{t})f'(X_{t})\right)\mathrm {d} t+f(X_{t})\mathrm {d} W_{t}$

for a given differentiable function f is equivalent to the Stratonovich SDE

$\mathrm {d} X_{t}=\alpha f(X_{t})\mathrm {d} t+f(X_{t})\circ W_{t}$

which is reducible to

$\mathrm {d} Y_{t}=\alpha \mathrm {d} t+\mathrm {d} W_{t}$

where $Y_{t}=h(X_{t})$ where h is defined as before. Its general solution is

$X_{t}=h^{-1}(\alpha t+W_{t}+h(X_{0}))$

## SDEs and supersymmetry

In supersymmetric theory of SDEs, stochastic dynamics is defined via stochastic evolution operator acting on the differential forms on the phase/state space of the model. In this formulation of stochastic dynamics, all SDEs possess topological supersymmetry which represents the preservation of the continuity of the phase space by continuous time flow. The spontaneous breakdown of this supersymmetry is the mathematical essence of the ubiquitous dynamical phenomenon known across disciplines as chaos.
