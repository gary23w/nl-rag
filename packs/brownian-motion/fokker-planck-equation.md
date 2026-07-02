---
title: "Fokker–Planck equation"
source: https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation
domain: brownian-motion
license: CC-BY-SA-4.0
tags: brownian motion, diffusion process, fokker-planck equation, ornstein-uhlenbeck process
fetched: 2026-07-02
---

# Fokker–Planck equation

In statistical mechanics and information theory, the **Fokker–Planck equation** is a partial differential equation that describes the time evolution of the probability density function of the position or velocity of a particle under the influence of drag forces and random forces, as in Brownian motion. The equation can be generalized to other observables as well. The Fokker–Planck equation has multiple applications in information theory, graph theory, data science, finance, economics, etc.

It is named after Adriaan Fokker and Max Planck, who described it in 1914 and 1917. It is also known as the **Kolmogorov forward equation**, after Andrey Kolmogorov, who independently discovered it in 1931. When applied to particle position distributions, it is better known as the **Smoluchowski equation** (after Marian Smoluchowski), and in this context it is equivalent to the convection–diffusion equation. When applied to particle position and momentum distributions, it is known as the Klein–Kramers equation. The case with zero diffusion is the continuity equation. The Fokker–Planck equation is obtained from the master equation through Kramers–Moyal expansion.

The first consistent microscopic derivation of the Fokker–Planck equation in the single scheme of classical and quantum mechanics was performed by Nikolay Bogoliubov and Nikolay Krylov.

## One dimension

In one spatial dimension *x*, for an Itô process driven by the standard Wiener process $W_{t}$ and described by the stochastic differential equation (SDE) $dX_{t}=\mu (X_{t},t)\,dt+\sigma (X_{t},t)\,dW_{t}$

with drift $\mu (X_{t},t)$ and diffusion coefficient $D(X_{t},t)=\sigma ^{2}(X_{t},t)/2$ , the Fokker–Planck equation for the probability density $p(x,t)$ of the random variable $X_{t}$ is

${\frac {\partial }{\partial t}}p(x,t)=-{\frac {\partial }{\partial x}}\left[\mu (x,t)p(x,t)\right]+{\frac {\partial ^{2}}{\partial x^{2}}}\left[D(x,t)p(x,t)\right].$

Link between the Itô SDE and the Fokker–Planck equation

In the following, use $\sigma ={\sqrt {2D}}$ .

Define the infinitesimal generator ${\mathcal {L}}$ (the following can be found in Ref.): ${\mathcal {L}}p(X_{t})=\lim _{\Delta t\to 0}{\frac {1}{\Delta t}}\left(\mathbb {E} {\big [}p(X_{t+\Delta t})\mid X_{t}=x{\big ]}-p(x)\right).$

The *transition probability* $\mathbb {P} _{t,t'}(x\mid x')$ , the probability of going from $(t',x')$ to $(t,x)$ , is introduced here; the expectation can be written as $\mathbb {E} (p(X_{t+\Delta t})\mid X_{t}=x)=\int p(y)\,\mathbb {P} _{t+\Delta t,t}(y\mid x)\,dy.$ Now we replace in the definition of ${\mathcal {L}}$ , multiply by $\mathbb {P} _{t,t'}(x\mid x')$ and integrate over $dx$ . The limit is taken on $\int p(y)\int \mathbb {P} _{t+\Delta t,t}(y\mid x)\,\mathbb {P} _{t,t'}(x\mid x')\,dx\,dy-\int p(x)\,\mathbb {P} _{t,t'}(x\mid x')\,dx.$ Note now that $\int \mathbb {P} _{t+\Delta t,t}(y\mid x)\,\mathbb {P} _{t,t'}(x\mid x')\,dx=\mathbb {P} _{t+\Delta t,t'}(y\mid x'),$ which is the Chapman–Kolmogorov theorem. Changing the dummy variable y to x , one gets ${\begin{aligned}\int p(x)\lim _{\Delta t\to 0}{\frac {1}{\Delta t}}\left(\mathbb {P} _{t+\Delta t,t'}(x\mid x')-\mathbb {P} _{t,t'}(x\mid x')\right)\,dx,\end{aligned}}$ which is a time derivative. Finally we arrive to $\int [{\mathcal {L}}p(x)]\mathbb {P} _{t,t'}(x\mid x')\,dx=\int p(x)\,{\frac {\partial }{\partial t}}\mathbb {P} _{t,t'}(x\mid x')\,dx.$ From here, the Kolmogorov backward equation can be deduced. If we instead use the adjoint operator of ${\mathcal {L}}$ , ${\mathcal {L}}^{\dagger }$ , defined such that $\int [{\mathcal {L}}p(x)]\mathbb {P} _{t,t'}(x\mid x')\,dx=\int p(x)[{\mathcal {L}}^{\dagger }\mathbb {P} _{t,t'}(x\mid x')]\,dx,$ then we arrive to the Kolmogorov forward equation, or Fokker–Planck equation, which, simplifying the notation $p(x,t)=\mathbb {P} _{t,t'}(x\mid x')$ , in its differential form reads ${\mathcal {L}}^{\dagger }p(x,t)={\frac {\partial }{\partial t}}p(x,t).$

Remains the issue of defining explicitly ${\mathcal {L}}$ . This can be done taking the expectation from the integral form of the Itô's lemma: $\mathbb {E} {\big (}p(X_{t}){\big )}=p(X_{0})+\mathbb {E} \left(\int _{0}^{t}\left({\frac {\partial }{\partial t}}+\mu {\frac {\partial }{\partial x}}+{\frac {\sigma ^{2}}{2}}{\frac {\partial ^{2}}{\partial x^{2}}}\right)p(X_{t'})\,dt'\right).$

The part that depends on $dW_{t}$ vanished because of the martingale property.

Then, for a particle subject to an Itô equation, using ${\mathcal {L}}=\mu {\frac {\partial }{\partial x}}+{\frac {\sigma ^{2}}{2}}{\frac {\partial ^{2}}{\partial x^{2}}},$ it can be easily calculated, using integration by parts, that ${\mathcal {L}}^{\dagger }=-{\frac {\partial }{\partial x}}(\mu \cdot )+{\frac {1}{2}}{\frac {\partial ^{2}}{\partial x^{2}}}\left(\sigma ^{2}\cdot \right),$ which bring us to the Fokker–Planck equation: ${\frac {\partial }{\partial t}}p(x,t)=-{\frac {\partial }{\partial x}}{\big (}\mu (x,t)\cdot p(x,t){\big )}+{\frac {\partial ^{2}}{\partial x^{2}}}\left({\frac {\sigma (x,t)^{2}}{2}}\,p(x,t)\right).$

The Fokker–Planck equation is used with problems where the initial distribution is known. If, instead, a final point is fixed, the Feynman–Kac formula can be used to calculate expectation values such as mean first-passage times, which is a consequence of the Kolmogorov backward equation. If the problem is to know the distribution at previous times, starting from a known distribution at later times, a reverse-time Fokker-Planck equation can be constructed.

The stochastic process defined above in the Itô sense can be rewritten within the Stratonovich convention as a Stratonovich SDE: $dX_{t}=\left[\mu (X_{t},t)-{\frac {1}{2}}{\frac {\partial }{\partial X_{t}}}D(X_{t},t)\right]\,dt+{\sqrt {2D(X_{t},t)}}\circ dW_{t}.$ It includes an added noise-induced drift term due to diffusion gradient effects if the noise is state-dependent. This convention is more often used in physical applications. Indeed, it is well known that any solution to the Stratonovich SDE is a solution to the Itô SDE.

The zero-drift equation with constant diffusion can be considered as a model of classical Brownian motion: ${\frac {\partial }{\partial t}}p(x,t)=D_{0}{\frac {\partial ^{2}}{\partial x^{2}}}\left[p(x,t)\right].$

This model has discrete spectrum of solutions if the condition of fixed boundaries is added for $\{0\leq x\leq L\}$ : ${\begin{aligned}p(0,t)&=p(L,t)=0,\\p(x,0)&=p_{0}(x).\end{aligned}}$

It has been shown that in this case an analytical spectrum of solutions allows deriving a local uncertainty relation for the coordinate-velocity phase volume: $\Delta x\,\Delta v\geq D_{0}.$ Here $D_{0}$ is a minimal value of a corresponding diffusion spectrum $D_{j}$ , while $\Delta x$ and $\Delta v$ represent the uncertainty of coordinate–velocity definition.

## Higher dimensions

More generally, if

$d\mathbf {X} _{t}={\boldsymbol {\mu }}(\mathbf {X} _{t},t)\,dt+{\boldsymbol {\sigma }}(\mathbf {X} _{t},t)\,d\mathbf {W} _{t},$

where $\mathbf {X} _{t}$ and ${\boldsymbol {\mu }}(\mathbf {X} _{t},t)$ are N-dimensional vectors, ${\boldsymbol {\sigma }}(\mathbf {X} _{t},t)$ is an $N\times M$ matrix and $\mathbf {W} _{t}$ is an *M*-dimensional standard Wiener process, the probability density $p(\mathbf {x} ,t)$ for $\mathbf {X} _{t}$ satisfies the Fokker–Planck equation

${\frac {\partial p(\mathbf {x} ,t)}{\partial t}}=-\sum _{i=1}^{N}{\frac {\partial }{\partial x_{i}}}\left[\mu _{i}(\mathbf {x} ,t)p(\mathbf {x} ,t)\right]+\sum _{i=1}^{N}\sum _{j=1}^{N}{\frac {\partial ^{2}}{\partial x_{i}\,\partial x_{j}}}\left[D_{ij}(\mathbf {x} ,t)p(\mathbf {x} ,t)\right],$

with drift vector ${\boldsymbol {\mu }}=(\mu _{1},\ldots ,\mu _{N})$ and diffusion tensor ${\textstyle \mathbf {D} ={\frac {1}{2}}{\boldsymbol {\sigma \sigma }}^{\mathsf {T}}}$ , i.e. $D_{ij}(\mathbf {x} ,t)={\frac {1}{2}}\sum _{k=1}^{M}\sigma _{ik}(\mathbf {x} ,t)\sigma _{jk}(\mathbf {x} ,t).$

If instead of an Itô SDE, a Stratonovich SDE is considered,

$d\mathbf {X} _{t}={\boldsymbol {\mu }}(\mathbf {X} _{t},t)\,dt+{\boldsymbol {\sigma }}(\mathbf {X} _{t},t)\circ d\mathbf {W} _{t},$

the Fokker–Planck equation will read:

${\frac {\partial p(\mathbf {x} ,t)}{\partial t}}=-\sum _{i=1}^{N}{\frac {\partial }{\partial x_{i}}}\left[\mu _{i}(\mathbf {x} ,t)\,p(\mathbf {x} ,t)\right]+{\frac {1}{2}}\sum _{k=1}^{M}\sum _{i=1}^{N}{\frac {\partial }{\partial x_{i}}}\left\{\sigma _{ik}(\mathbf {x} ,t)\sum _{j=1}^{N}{\frac {\partial }{\partial x_{j}}}\left[\sigma _{jk}(\mathbf {x} ,t)\,p(\mathbf {x} ,t)\right]\right\}$

## Generalization

In general, the Fokker–Planck equations are a special case to the general Kolmogorov forward equation

${\frac {\partial }{\partial t}}\rho ={\mathcal {A}}^{*}\rho$

where the linear operator ${\mathcal {A}}^{*}$ is the Hermitian adjoint to the infinitesimal generator for the Markov process.

## Examples

### Wiener process

A standard scalar Wiener process is generated by the stochastic differential equation

$dX_{t}=dW_{t}.$

Here the drift term is zero and the diffusion coefficient is 1/2. Thus the corresponding Fokker–Planck equation is

${\frac {\partial p(x,t)}{\partial t}}={\frac {1}{2}}{\frac {\partial ^{2}p(x,t)}{\partial x^{2}}},$

which is the simplest form of a diffusion equation. If the initial condition is $p(x,0)=\delta (x)$ , the solution is

$p(x,t)={\frac {1}{\sqrt {2\pi t}}}e^{-{x^{2}}/({2t})}.$

### Boltzmann distribution at the thermodynamic equilibrium

The overdamped Langevin equation $dx_{t}=-{\frac {1}{k_{\text{B}}T}}{\frac {dU}{dx}}\,dt+dW_{t}$ gives ${\textstyle \partial _{t}p={\frac {1}{2}}\nabla \cdot \left({\frac {p}{k_{\text{B}}T}}\nabla U+\nabla p\right)}$ . The Boltzmann distribution $p(x)\propto e^{-U(x)/k_{\text{B}}T}$ is an equilibrium distribution, and assuming U grows sufficiently rapidly (that is, the potential well is deep enough to confine the particle), the Boltzmann distribution is the unique equilibrium.

### Ornstein–Uhlenbeck process

The Ornstein–Uhlenbeck process is a process defined as

$dX_{t}=-aX_{t}\,dt+\sigma \,dW_{t}.$

with $a>0$ . Physically, this equation can be motivated as follows: a particle of mass m with velocity $V_{t}$ moving in a medium, e.g., a fluid, will experience a friction force which resists motion whose magnitude can be approximated as being proportional to particle's velocity $-aV_{t}$ with $a=\mathrm {constant}$ . Other particles in the medium will randomly kick the particle as they collide with it and this effect can be approximated by a white noise term; $\sigma (dW_{t}/dt)$ . Newton's second law is written as

$m{\frac {dV_{t}}{dt}}=-aV_{t}+\sigma {\frac {dW_{t}}{dt}}.$

Taking $m=1$ for simplicity and changing the notation as $V_{t}\rightarrow X_{t}$ leads to the familiar form $dX_{t}=-aX_{t}dt+\sigma dW_{t}$ .

The corresponding Fokker–Planck equation is ${\frac {\partial p(x,t)}{\partial t}}=a{\frac {\partial }{\partial x}}\left(x\,p(x,t)\right)+{\frac {\sigma ^{2}}{2}}{\frac {\partial ^{2}p(x,t)}{\partial x^{2}}},$

The stationary solution ( $\partial _{t}p=0$ ) is $p_{ss}(x)={\sqrt {\frac {a}{\pi \sigma ^{2}}}}e^{-{ax^{2}}/{\sigma ^{2}}}.$

### Plasma physics

In plasma physics, the distribution function for a particle species s , $p_{s}(\mathbf {x} ,\mathbf {v} ,t)$ , takes the place of the probability density function. The corresponding Boltzmann equation is given by

${\frac {\partial p_{s}}{\partial t}}+\mathbf {v} \cdot {\boldsymbol {\nabla }}p_{s}+{\frac {Z_{s}e}{m_{s}}}\left(\mathbf {E} +\mathbf {v} \times \mathbf {B} \right)\cdot {\boldsymbol {\nabla }}_{v}p_{s}=-{\frac {\partial }{\partial v_{i}}}\left(p_{s}\langle \Delta v_{i}\rangle \right)+{\frac {1}{2}}{\frac {\partial ^{2}}{\partial v_{i}\,\partial v_{j}}}\left(p_{s}\langle \Delta v_{i}\,\Delta v_{j}\rangle \right),$

where the third term includes the particle acceleration due to the Lorentz force and the Fokker–Planck term at the right-hand side represents the effects of particle collisions. The quantities $\langle \Delta v_{i}\rangle$ and $\langle \Delta v_{i}\,\Delta v_{j}\rangle$ are the average change in velocity a particle of type s experiences due to collisions with all other particle species in unit time. Expressions for these quantities are given elsewhere. If collisions are ignored, the Boltzmann equation reduces to the Vlasov equation.

## Smoluchowski diffusion equation

Consider an overdamped Brownian particle under external force $F(r)$ : $m{\ddot {r}}=-\gamma {\dot {r}}+F(r)+\sigma \xi (t)$ where the $m{\ddot {r}}$ term is negligible (the meaning of "overdamped"). Thus, it is just $\gamma \,dr=F(r)\,dt+\sigma \,dW_{t}$ . The Fokker–Planck equation for this particle is the Smoluchowski diffusion equation: ${\frac {\partial }{\partial t}}P(r,t\mid r_{0},t_{0})=\nabla \cdot \left[D\left(\nabla -\beta F(r)\right)P(r,t\mid r_{0},t_{0})\right]$ where D is the diffusion constant and $\beta ={\frac {1}{k_{\text{B}}T}}$ . The importance of this equation is it allows for both the inclusion of the effect of temperature on the system of particles and a spatially dependent diffusion constant.

Derivation of the Smoluchowski equation from the Fokker–Planck equation

Starting with the Langevin Equation of a Brownian particle in external field $F(r)$ , where $\gamma$ is the friction term, $\xi$ is a fluctuating force on the particle, and $\sigma$ is the amplitude of the fluctuation.

$m{\ddot {r}}=-\gamma {\dot {r}}+F(r)+\sigma \xi (t)$

At equilibrium the frictional force is much greater than the inertial force, $\left\vert \gamma {\dot {r}}\right\vert \gg \left\vert m{\ddot {r}}\right\vert$ . Therefore, the Langevin equation becomes,

$\gamma {\dot {r}}=F(r)+\sigma \xi (t),$

which generates the following Fokker–Planck equation,

${\frac {\partial }{\partial t}}P(r,t\mid r_{0},t_{0})=\left(\nabla ^{2}{\frac {\sigma ^{2}}{2\gamma ^{2}}}-\nabla \cdot {\frac {F(r)}{\gamma }}\right)P(r,t\mid r_{0},t_{0}).$

Rearranging the Fokker–Planck equation,

${\frac {\partial }{\partial t}}P(r,t|r_{0},t_{0})=\nabla \cdot \left(\nabla D-{\frac {F(r)}{\gamma }}\right)P(r,t|r_{0},t_{0})$

where $D={\frac {\sigma ^{2}}{2\gamma ^{2}}}$ . **Note**, the diffusion coefficient may not necessarily be spatially independent if $\sigma$ or $\gamma$ are spatially dependent.

Next, the total number of particles in any particular volume is given by,

$N_{V}(t|r_{0},t_{0})=\int _{V}drP(r,t\mid r_{0},t_{0})$

Therefore, the flux of particles can be determined by taking the time derivative of the number of particles in a given volume, plugging in the Fokker–Planck equation, and then applying Gauss's Theorem.

${\frac {\partial }{\partial t}}N_{V}(t|r_{0},t_{0})=\int _{V}dV\,\nabla \cdot \left(\nabla D-{\frac {F(r)}{\gamma }}\right)P(r,t\mid r_{0},t_{0})=\int _{\partial V}\,d\mathbf {a} \cdot j(r,t\mid r_{0},t_{0})$

$j(r,t\mid r_{0},t_{0})=\left(\nabla D-{\frac {F(r)}{\gamma }}\right)P(r,t\mid r_{0},t_{0})$

In equilibrium, it is assumed that the flux goes to zero. Therefore, Boltzmann statistics can be applied for the probability of a particles location at equilibrium, where $F(r)=-\nabla U(r)$ is a conservative force and the probability of a particle being in a state r is given as $P(r,t\mid r_{0},t_{0})={\frac {e^{-\beta U(r)}}{Z}}$ .

$j(r,t\mid r_{0},t_{0})=\left(\nabla D-{\frac {F(r)}{\gamma }}\right){\frac {e^{-\beta U(r)}}{Z}}=0$

$\Rightarrow \nabla D=F(r)\left({\frac {1}{\gamma }}-D\beta \right)$

This relation is a realization of the fluctuation–dissipation theorem. Now applying $\nabla \cdot \nabla$ to $DP(r,t|r_{0},t_{0})$ and using the Fluctuation-dissipation theorem,

${\begin{aligned}\nabla \cdot \nabla DP(r,t\mid r_{0},t_{0})&=\nabla \cdot D\nabla P(r,t\mid r_{0},t_{0})+\nabla \cdot P(r,t|r_{0},t_{0})\nabla D\\&=\nabla \cdot D\nabla P(r,t\mid r_{0},t_{0})+\nabla \cdot P(r,t\mid r_{0},t_{0}){\frac {F(r)}{\gamma }}-\nabla \cdot P(r,t\mid r_{0},t_{0})D\beta F(r)\end{aligned}}$

Rearranging,

$\Rightarrow \nabla \cdot \left(\nabla D-{\frac {F(r)}{\gamma }}\right)P(r,t\mid r_{0},t_{0})=\nabla \cdot D(\nabla -\beta F(r))P(r,t\mid r_{0},t_{0})$

Therefore, the Fokker–Planck equation becomes the Smoluchowski equation, ${\frac {\partial }{\partial t}}P(r,t\mid r_{0},t_{0})=\nabla \cdot D(\nabla -\beta F(r))P(r,t\mid r_{0},t_{0})$

for an arbitrary force

$F(r)$

.

## Computational considerations

Brownian motion follows the Langevin equation, which can be solved for many different stochastic forcings with results being averaged (canonical ensemble in molecular dynamics). However, instead of this computationally intensive approach, one can use the Fokker–Planck equation and consider the probability $p(\mathbf {v} ,t)\,d\mathbf {v}$ of the particle having a velocity in the interval $(\mathbf {v} ,\mathbf {v} +d\mathbf {v} )$ when it starts its motion with $\mathbf {v} _{0}$ at time 0.

### 1-D linear potential example

Brownian dynamics in one dimension is simple.

#### Theory

Starting with a linear potential of the form $U(x)=cx$ the corresponding Smoluchowski equation becomes,

${\frac {\partial }{\partial t}}P(x,t\mid x_{0},t_{0})={\frac {\partial }{\partial x}}D\left({\frac {\partial }{\partial x}}+\beta c\right)P(x,t\mid x_{0},t_{0})$

where the diffusion constant, D , is constant over space and time. The boundary conditions are such that the probability vanishes at $x\rightarrow \pm \infty$ with an initial condition of the ensemble of particles starting in the same place, $P(x,t{=}t_{0}|x_{0},t_{0})=\delta (x-x_{0})$ .

Defining $\tau =Dt$ and $b=\beta c$ and applying the coordinate transformation,

$y=x+\tau b,\ \ \ y_{0}=x_{0}+\tau _{0}b$

With $P(x,t,|x_{0},t_{0})=q(y,\tau \mid y_{0},\tau _{0})$ the Smoluchowki equation becomes, ${\frac {\partial }{\partial \tau }}q(y,\tau \mid y_{0},\tau _{0})={\frac {\partial ^{2}}{\partial y^{2}}}q(y,\tau \mid y_{0},\tau _{0}),$

which is the free diffusion equation with solution, $q(y,\tau \mid y_{0},\tau _{0})={\frac {1}{\sqrt {4\pi (\tau -\tau _{0})}}}e^{-{\frac {(y-y_{0})^{2}}{4(\tau -\tau _{0})}}}.$

And after transforming back to the original coordinates, $P(x,t\mid x_{0},t_{0})={\frac {1}{\sqrt {4\pi D(t-t_{0})}}}\exp {\left[{-{\frac {\left(x-x_{0}+D\beta c\left(t-t_{0}\right)\right)^{2}}{4D\left(t-t_{0}\right)}}}\right]}$

#### Simulation

The simulation on the right was completed using a Brownian dynamics simulation. Starting with a Langevin equation for the system, $m{\ddot {x}}=-\gamma {\dot {x}}-c+\sigma \xi (t)$ where $\gamma$ is the friction term, $\xi$ is a fluctuating force on the particle, and $\sigma$ is the amplitude of the fluctuation. At equilibrium the frictional force is much greater than the inertial force, $\left|\gamma {\dot {x}}\right|\gg \left|m{\ddot {x}}\right|$ . Therefore, the Langevin equation becomes, $\gamma {\dot {x}}=-c+\sigma \xi (t)$

For the Brownian dynamic simulation the fluctuation force $\xi (t)$ is assumed to be Gaussian with the amplitude being dependent of the temperature of the system ${\textstyle \sigma ={\sqrt {2\gamma k_{\text{B}}T}}}$ . Rewriting the Langevin equation,

${\frac {dx}{dt}}=-D\beta c+{\sqrt {2D}}\xi (t)$ where ${\textstyle D={\frac {k_{\text{B}}T}{\gamma }}}$ is the Einstein relation. The integration of this equation was done using the Euler–Maruyama method to numerically approximate the path of this Brownian particle.

## Solution

Being a partial differential equation, the Fokker–Planck equation can be solved analytically only in special cases. A formal analogy of the Fokker–Planck equation with the Schrödinger equation allows the use of advanced operator techniques known from quantum mechanics for its solution in a number of cases. Furthermore, in the case of overdamped dynamics when the Fokker–Planck equation contains second partial derivatives with respect to all spatial variables, the equation can be written in the form of a master equation that can easily be solved numerically. In many applications, one is only interested in the steady-state probability distribution $p_{0}(x)$ , which can be found from ${\textstyle {\frac {\partial p(x,t)}{\partial t}}=0}$ . The computation of mean first passage times and splitting probabilities can be reduced to the solution of an ordinary differential equation which is intimately related to the Fokker–Planck equation.

## Particular cases with known solution and inversion

In mathematical finance for volatility smile modeling of options via local volatility, one has the problem of deriving a diffusion coefficient ${\sigma }(\mathbf {X} _{t},t)$ consistent with a probability density obtained from market option quotes. The problem is therefore an inversion of the Fokker–Planck equation: Given the density f(x,t) of the option underlying *X* deduced from the option market, one aims at finding the local volatility ${\sigma }(\mathbf {X} _{t},t)$ consistent with *f*. This is an inverse problem that has been solved in general by Dupire (1994, 1997) with a non-parametric solution. Brigo and Mercurio (2002, 2003) propose a solution in parametric form via a particular local volatility ${\sigma }(\mathbf {X} _{t},t)$ consistent with a solution of the Fokker–Planck equation given by a mixture model. More information is available also in Fengler (2008), Gatheral (2008), and Musiela and Rutkowski (2008).

## Fokker–Planck equation and path integral

Every Fokker–Planck equation is equivalent to a path integral. The path integral formulation is an excellent starting point for the application of field theory methods. This is used, for instance, in critical dynamics.

A derivation of the path integral is possible in a similar way as in quantum mechanics. The derivation for a Fokker–Planck equation with one variable x is as follows. Start by inserting a delta function and then integrating by parts:

${\begin{aligned}{\frac {\partial }{\partial t}}p{\left(x',t\right)}&=-{\frac {\partial }{\partial x'}}\left[D_{1}(x',t)p(x',t)\right]+{\frac {\partial ^{2}}{\partial {x'}^{2}}}\left[D_{2}(x',t)p(x',t)\right]\\[1ex]&=\int _{-\infty }^{\infty }dx\left[\left(D_{1}{\left(x,t\right)}{\frac {\partial }{\partial x}}+D_{2}{\left(x,t\right)}{\frac {\partial ^{2}}{\partial x^{2}}}\right)\delta {\left(x'-x\right)}\right]p(x,t).\end{aligned}}$

The x -derivatives here only act on the $\delta$ -function, not on $p(x,t)$ . Integrate over a time interval $\varepsilon$ ,

$p(x',t{+}\varepsilon )=\int _{-\infty }^{\infty }\,dx\left[\left(1+\varepsilon D_{1}(x,t){\frac {\partial }{\partial x}}+\varepsilon D_{2}(x,t){\frac {\partial ^{2}}{\partial x^{2}}}\right)\delta (x'-x)\right]p(x,t)+O(\varepsilon ^{2}).$

Insert the Fourier integral

$\delta {\left(x'-x\right)}=\int _{-i\infty }^{i\infty }{\frac {d{\tilde {x}}}{2\pi i}}e^{{\tilde {x}}{\left(x-x'\right)}}$

for the $\delta$ -function,

${\begin{aligned}p(x',t+\varepsilon )&=\int _{-\infty }^{\infty }dx\int _{-i\infty }^{i\infty }{\frac {d{\tilde {x}}}{2\pi i}}\left(1+\varepsilon \left[{\tilde {x}}D_{1}(x,t)+{\tilde {x}}^{2}D_{2}(x,t)\right]\right)e^{{\tilde {x}}(x-x')}p(x,t)+O(\varepsilon ^{2})\\[5pt]&=\int _{-\infty }^{\infty }dx\int _{-i\infty }^{i\infty }{\frac {d{\tilde {x}}}{2\pi i}}\exp \left(\varepsilon \left[-{\tilde {x}}{\frac {(x'-x)}{\varepsilon }}+{\tilde {x}}D_{1}(x,t)+{\tilde {x}}^{2}D_{2}(x,t)\right]\right)p(x,t)+O(\varepsilon ^{2}).\end{aligned}}$

This equation expresses $p(x',t{+}\varepsilon )$ as functional of $p(x,t)$ . Iterating $(t'-t)/\varepsilon$ times and performing the limit $\varepsilon \rightarrow 0$ gives a path integral with action

$S=\int dt\left[{\tilde {x}}D_{1}(x,t)+{\tilde {x}}^{2}D_{2}(x,t)-{\tilde {x}}{\frac {\partial x}{\partial t}}\right].$

The variables ${\tilde {x}}$ conjugate to x are called "response variables".

Although formally equivalent, different problems may be solved more easily in the Fokker–Planck equation or the path integral formulation. The equilibrium distribution for instance may be obtained more directly from the Fokker–Planck equation.
