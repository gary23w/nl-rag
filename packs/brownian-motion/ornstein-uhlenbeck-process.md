---
title: "Ornstein–Uhlenbeck process"
source: https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process
domain: brownian-motion
license: CC-BY-SA-4.0
tags: brownian motion, diffusion process, fokker-planck equation, ornstein-uhlenbeck process
fetched: 2026-07-02
---

# Ornstein–Uhlenbeck process

In mathematics, the **Ornstein–Uhlenbeck process** is a stochastic process with applications in financial mathematics and the physical sciences. Its original application in physics was as a model for the velocity of a massive Brownian particle under the influence of friction. It is named after Leonard Ornstein and George Eugene Uhlenbeck.

The Ornstein–Uhlenbeck process is a stationary Gauss–Markov process, which means that it is a Gaussian process, a Markov process, and is temporally homogeneous. In fact, it is the only nontrivial process that satisfies these three conditions, up to allowing linear transformations of the space and time variables. Over time, the process tends to drift towards its mean function: such a process is called ***mean-reverting***.

The process can be considered to be a modification of the random walk in continuous time, or Wiener process, in which the properties of the process have been changed so that there is a tendency of the walk to move back towards a central location, with a greater attraction when the process is further away from the center. The Ornstein–Uhlenbeck process can also be considered as the continuous-time analogue of the discrete-time AR(1) process.

## Definition

The Ornstein–Uhlenbeck process $x_{t}$ is defined by the following stochastic differential equation:

$dx_{t}=-\theta \,x_{t}\,dt+\sigma \,dW_{t}$

where $\theta >0$ and $\sigma >0$ are parameters and $W_{t}$ denotes the Wiener process.

An additional term is sometimes added:

$dx_{t}=-\theta (x_{t}-\mu )\,dt+\sigma \,dW_{t}$

where $\mu$ is a constant called the (long-term) mean. The Ornstein–Uhlenbeck process is sometimes also written as a Langevin equation of the form

${\frac {dx_{t}}{dt}}=-\theta \,x_{t}+\sigma \,\eta (t)$

where $\eta (t)$ , also known as white noise, stands in for the supposed derivative $dW_{t}/dt$ of the Wiener process. However, $dW_{t}/dt$ does not exist because the Wiener process is nowhere differentiable, and so the Langevin equation only makes sense if interpreted in distributional sense. In physics and engineering disciplines, it is a common representation for the Ornstein–Uhlenbeck process and similar stochastic differential equations by tacitly assuming that the noise term is a derivative of a differentiable (e.g. Fourier) interpolation of the Wiener process.

## Fokker–Planck equation representation

The Ornstein–Uhlenbeck process can also be described in terms of a probability density function, $P(x,t)$ , which specifies the probability of finding the process in the state x at time t . This function satisfies the Fokker–Planck equation

${\frac {\partial P}{\partial t}}=\theta {\frac {\partial }{\partial x}}((x-\mu )P)+D{\frac {\partial ^{2}P}{\partial x^{2}}}$

where $D=\sigma ^{2}/2$ . This is a linear parabolic partial differential equation which can be solved by a variety of techniques. The transition probability, also known as the Green's function, $P(x,t\mid x_{0},t_{0})$ is a Gaussian with mean $x_{0}e^{-\theta (t-t_{0})}+\mu (1-e^{-\theta (t-t_{0})})$ and variance ${\frac {D}{\theta }}\left(1-e^{-2\theta (t-t_{0})}\right)$ :

$P(x,t\mid x_{0},t_{0})={\sqrt {\frac {\theta }{2\pi D(1-e^{-2\theta (t-t_{0})})}}}\exp \left[-{\frac {\theta }{2D}}{\frac {(x-x_{0}e^{-\theta (t-t_{0})}-\mu (1-e^{-\theta (t-t_{0})}))^{2}}{1-e^{-2\theta (t-t_{0})}}}\right]$

This gives the probability of the state x occurring at time t given initial state $x_{0}$ at time $t_{0}<t$ . Equivalently, $P(x,t\mid x_{0},t_{0})$ is the solution of the Fokker–Planck equation with initial condition $P(x,t_{0})=\delta (x-x_{0})$ .

## Mathematical properties

Conditioned on a particular value of $x_{0}$ , the mean is

$\operatorname {\mathbb {E} } (x_{t}\mid x_{0})=x_{0}e^{-\theta t}+\mu (1-e^{-\theta t})$

and the covariance is

$\operatorname {cov} (x_{s},x_{t})={\frac {\sigma ^{2}}{2\theta }}\left(e^{-\theta |t-s|}-e^{-\theta (t+s)}\right).$

For the stationary (unconditioned) process, the mean of $x_{t}$ is $\mu$ , and the covariance of $x_{s}$ and $x_{t}$ is ${\frac {\sigma ^{2}}{2\theta }}e^{-\theta |t-s|}$ .

The Ornstein–Uhlenbeck process is an example of a Gaussian process that has a bounded variance and admits a stationary probability distribution, in contrast to the Wiener process; the difference between the two is in their "drift" term. For the Wiener process the drift term is constant, whereas for the Ornstein–Uhlenbeck process it is dependent on the current value of the process: if the current value of the process is less than the (long-term) mean, the drift will be positive; if the current value of the process is greater than the (long-term) mean, the drift will be negative. In other words, the mean acts as an equilibrium level for the process. This gives the process its informative name, "mean-reverting."

### Properties of sample paths

A temporally homogeneous Ornstein–Uhlenbeck process starting at $x_{0}=0$ can be represented as a scaled, time-transformed Wiener process:

$x_{t}={\frac {\sigma }{\sqrt {2\theta }}}e^{-\theta t}W_{e^{2\theta t}-1}$

where $W_{t}$ is the standard Wiener process. This is roughly Theorem 1.2 in Doob 1942. Equivalently, with the change of variable $s=e^{2\theta t}$ this becomes

$W_{s}={\frac {\sqrt {2\theta }}{\sigma }}s^{1/2}x_{(\ln s)/(2\theta )},\qquad s>0$

Using this mapping, one can translate known properties of $W_{t}$ into corresponding statements for $x_{t}$ . For instance, the law of the iterated logarithm for $W_{t}$ becomes

$\limsup _{t\to \infty }{\frac {x_{t}}{\sqrt {(\sigma ^{2}/\theta )\ln t}}}=1,\quad {\text{with probability 1.}}$

### Formal solution

The stochastic differential equation for $x_{t}$ can be formally solved by variation of parameters. Writing

$f(x_{t},t)=x_{t}e^{\theta t}\,$

we get

${\begin{aligned}df(x_{t},t)&=\theta \,x_{t}\,e^{\theta t}\,dt+e^{\theta t}\,dx_{t}\\[6pt]&=e^{\theta t}\theta \,\mu \,dt+\sigma \,e^{\theta t}\,dW_{t}.\end{aligned}}$

Integrating from 0 to t we get

$x_{t}e^{\theta t}=x_{0}+\int _{0}^{t}e^{\theta s}\theta \,\mu \,ds+\int _{0}^{t}\sigma \,e^{\theta s}\,dW_{s}\,$

whereupon we see

$x_{t}=x_{0}\,e^{-\theta t}+\mu \,(1-e^{-\theta t})+\sigma \int _{0}^{t}e^{-\theta (t-s)}\,dW_{s}.\,$

From this representation, the first moment (i.e. the mean) is shown to be

$\operatorname {E} (x_{t})=x_{0}e^{-\theta t}+\mu (1-e^{-\theta t})\!\$

assuming $x_{0}$ is constant. Moreover, the Itō isometry can be used to calculate the covariance function by

${\begin{aligned}\operatorname {cov} (x_{s},x_{t})&=\operatorname {E} [(x_{s}-\operatorname {E} [x_{s}])(x_{t}-\operatorname {E} [x_{t}])]\\[5pt]&=\operatorname {E} \left[\int _{0}^{s}\sigma e^{\theta (u-s)}\,dW_{u}\int _{0}^{t}\sigma e^{\theta (v-t)}\,dW_{v}\right]\\[5pt]&=\sigma ^{2}e^{-\theta (s+t)}\operatorname {E} \left[\int _{0}^{s}e^{\theta u}\,dW_{u}\int _{0}^{t}e^{\theta v}\,dW_{v}\right]\\[5pt]&={\frac {\sigma ^{2}}{2\theta }}\,e^{-\theta (s+t)}(e^{2\theta \min(s,t)}-1)\\[5pt]&={\frac {\sigma ^{2}}{2\theta }}\left(e^{-\theta |t-s|}-e^{-\theta (t+s)}\right).\end{aligned}}$

### Kolmogorov equations

The infinitesimal generator of the process is $Lf=-\theta (x-\mu )f'+{\frac {1}{2}}\sigma ^{2}f''$ If we let $y=(x-\mu ){\sqrt {\frac {2\theta }{\sigma ^{2}}}}$ , then the eigenvalue equation simplifies to: ${\frac {d^{2}}{dy^{2}}}\phi -y{\frac {d}{dy}}\phi -{\frac {\lambda }{\theta }}\phi =0$ which is the defining equation for Hermite polynomials. Its solutions are $\phi (y)=He_{n}(y)$ , with $\lambda =-n\theta$ , which implies that the mean first passage time for a particle to hit a point on the boundary is on the order of $\theta ^{-1}$ .

## Numerical simulation

By using discretely sampled data at time intervals of width t , the maximum likelihood estimators for the parameters of the Ornstein–Uhlenbeck process are asymptotically normal to their true values. More precisely, ${\sqrt {n}}\left({\begin{pmatrix}{\widehat {\theta }}_{n}\\{\widehat {\mu }}_{n}\\{\widehat {\sigma }}_{n}^{2}\end{pmatrix}}-{\begin{pmatrix}\theta \\\mu \\\sigma ^{2}\end{pmatrix}}\right)\xrightarrow {d} \ {\mathcal {N}}\left({\begin{pmatrix}0\\0\\0\end{pmatrix}},{\begin{pmatrix}{\frac {e^{2t\theta }-1}{t^{2}}}&0&{\frac {\sigma ^{2}(e^{2t\theta }-1-2t\theta )}{t^{2}\theta }}\\0&{\frac {\sigma ^{2}\left(e^{t\theta }+1\right)}{2\left(e^{t\theta }-1\right)\theta }}&0\\{\frac {\sigma ^{2}(e^{2t\theta }-1-2t\theta )}{t^{2}\theta }}&0&{\frac {\sigma ^{4}\left[\left(e^{2t\theta }-1\right)^{2}+2t^{2}\theta ^{2}\left(e^{2t\theta }+1\right)+4t\theta \left(e^{2t\theta }-1\right)\right]}{t^{2}\left(e^{2t\theta }-1\right)\theta ^{2}}}\end{pmatrix}}\right)$

To simulate an OU process numerically with standard deviation $\Sigma$ and correlation time $\tau =1/\Theta$ , one method is to apply the finite-difference formula

$x(t+dt)=x(t)-\Theta \,dt\,x(t)+\Sigma {\sqrt {2\,dt\,\Theta }}\nu _{i}$ where $\nu _{i}$ is a normally distributed random number with zero mean and unit variance, sampled independently at every time-step $dt$ .

## Scaling limit interpretation

The Ornstein–Uhlenbeck process can be interpreted as a scaling limit of a discrete process, in the same way that Brownian motion is a scaling limit of random walks. Consider an urn containing n black and white balls. At each step a ball is chosen at random and replaced by a ball of the opposite colour. Let $X_{k}$ be the number of black balls in the urn after k steps. Then ${\frac {X_{[nt]}-n/2}{\sqrt {n}}}$ converges in law to an Ornstein–Uhlenbeck process as n tends to infinity. This was obtained by Mark Kac.

Heuristically one may obtain this as follows.

Let $X_{t}^{(n)}:={\frac {X_{[nt]}-n/2}{\sqrt {n}}}$ , and we will obtain the stochastic differential equation at the $n\to \infty$ limit. First deduce $\Delta t=1/n,\quad \Delta X_{t}^{(n)}=X_{t+\Delta t}^{(n)}-X_{t}^{(n)}.$ With this, we can calculate the mean and variance of $\Delta X_{t}^{(n)}$ , which turns out to be $-2X_{t}^{(n)}\Delta t$ and $\Delta t$ . Thus at the $n\to \infty$ limit, we have $dX_{t}=-2X_{t}\,dt+dW_{t}$ , with solution (assuming $X_{0}$ distribution is standard normal) $X_{t}=e^{-2t}W_{e^{4t}}$ .

## Applications

### In physics: noisy relaxation

The Ornstein–Uhlenbeck process is a prototype of a noisy relaxation process. A canonical example is a Hookean spring (harmonic oscillator) with spring constant k whose dynamics is overdamped with friction coefficient $\gamma$ . In the presence of thermal fluctuations with temperature T , the length $x(t)$ of the spring fluctuates around the spring rest length $x_{0}$ ; its stochastic dynamics is described by an Ornstein–Uhlenbeck process with

${\begin{aligned}\theta &=k/\gamma ,\\\mu &=x_{0},\\\sigma &={\sqrt {2D}}={\sqrt {2k_{B}T/\gamma }},\end{aligned}}$

where $\sigma ^{2}$ is derived from the Stokes–Einstein equation $D=k_{B}T/\gamma$ for the effective diffusion constant. Rewritten as Langevin equation as common in physics, $\gamma \,{\dot {x}}=-k(x-x_{0})+\xi (t)$ , where $\xi (t)$ denotes Gaussian white noise with $\langle \xi (t)\xi (t')\rangle =2D\,\delta (t-t')$ ; hence, we have for the auto-correlation function (same as above in mathematics notation) $\langle [x(t)-x_{0}][x(t')-x_{0}]\rangle =(k_{B}T/k)\exp[-(k/\gamma )|t-t'|]$ with variance $k_{B}T/k$ independent from $\gamma$ and relaxation time-scale $\gamma /k$ as expected from dimensional analysis.

This model has been used to characterize the motion of a Brownian particle in an optical trap. At equilibrium, the spring stores an average energy $\langle E\rangle =k\langle (x-x_{0})^{2}\rangle /2=k_{B}T/2$ in accordance with the equipartition theorem.

### In financial mathematics

The Ornstein–Uhlenbeck process is used in the Vasicek model of the interest rate. The Ornstein–Uhlenbeck process is one of several approaches used to model (with modifications) interest rates, currency exchange rates, and commodity prices stochastically. The parameter $\mu$ represents the equilibrium or mean value supported by fundamentals; $\sigma$ the degree of volatility around it caused by shocks, and $\theta$ the rate by which these shocks dissipate and the variable reverts towards the mean. One application of the process is a trading strategy known as pairs trade.

A further implementation of the Ornstein–Uhlenbeck process is derived by Marcello Minenna in order to model the stock return under a lognormal distribution dynamics. This modeling aims at the determination of confidence interval to predict market abuse phenomena.

### In evolutionary biology

The Ornstein–Uhlenbeck process has been proposed as an improvement over a Brownian motion model for modeling the change in organismal phenotypes over time. A Brownian motion model implies that the phenotype can move without limit, whereas for most phenotypes natural selection imposes a cost for moving too far in either direction. A meta-analysis of 250 fossil phenotype time-series showed that an Ornstein–Uhlenbeck model was the best fit for 115 (46%) of the examined time series, supporting stasis as a common evolutionary pattern. This said, there are certain challenges to its use: model selection mechanisms are often biased towards preferring an OU process without sufficient support, and misinterpretation is easy to the unsuspecting data scientist.

## Generalizations

It is possible to define a *Lévy-driven Ornstein–Uhlenbeck process*, in which the background driving process is a Lévy process instead of a Wiener process:

$dx_{t}=-\theta \,x_{t}\,dt+\sigma \,dL_{t}$

Here, the differential of the Wiener process $W_{t}$ has been replaced with the differential of a Lévy process $L_{t}$ .

In addition, in finance, stochastic processes are used where the volatility increases for larger values of X . In particular, the CKLS process (Chan–Karolyi–Longstaff–Sanders) with the volatility term replaced by $\sigma \,x^{\gamma }\,dW_{t}$ can be solved in closed form for $\gamma =1$ , as well as for $\gamma =0$ , which corresponds to the conventional OU process. Another special case is $\gamma =1/2$ , which corresponds to the Cox–Ingersoll–Ross model (CIR-model).

### Higher dimensions

A multi-dimensional version of the Ornstein–Uhlenbeck process, denoted by the *N*-dimensional vector $\mathbf {x} _{t}$ , can be defined from

$d\mathbf {x} _{t}=-{\boldsymbol {\beta }}\,\mathbf {x} _{t}\,dt+{\boldsymbol {\sigma }}\,d\mathbf {W} _{t}.$

where $\mathbf {W} _{t}$ is an *N*-dimensional Wiener process, and ${\boldsymbol {\beta }}$ and ${\boldsymbol {\sigma }}$ are constant *N*×*N* matrices. The solution is

$\mathbf {x} _{t}=e^{-{\boldsymbol {\beta }}t}\mathbf {x} _{0}+\int _{0}^{t}e^{-{\boldsymbol {\beta }}(t-t')}{\boldsymbol {\sigma }}\,d\mathbf {W} _{t'}$

and the mean is

$\operatorname {E} (\mathbf {x} _{t})=e^{-{\boldsymbol {\beta }}t}\operatorname {E} (\mathbf {x} _{0}).$

These expressions make use of the matrix exponential.

The process can also be described in terms of the probability density function $P(\mathbf {x} ,t)$ , which satisfies the Fokker–Planck equation

${\frac {\partial P}{\partial t}}=\sum _{i,j}\beta _{ij}{\frac {\partial }{\partial x_{i}}}(x_{j}P)+\sum _{i,j}D_{ij}{\frac {\partial ^{2}P}{\partial x_{i}\,\partial x_{j}}},$

where the matrix ${\boldsymbol {D}}$ with components $D_{ij}$ is defined by ${\boldsymbol {D}}={\boldsymbol {\sigma }}{\boldsymbol {\sigma }}^{T}/2$ . Like for the one-dimensional case, the process is a linear transformation of Gaussian random variables, and therefore itself must be Gaussian. Because of this, the transition probability $P(\mathbf {x} ,t\mid \mathbf {x} ',t')$ is a Gaussian which can be written down explicitly. If the real parts of the eigenvalues of ${\boldsymbol {\beta }}$ are larger than zero, a stationary solution $P_{\text{st}}(\mathbf {x} )$ moreover exists, given by

$P_{\text{st}}(\mathbf {x} )=(2\pi )^{-N/2}(\det {\boldsymbol {\omega }})^{-1/2}\exp \left(-{\frac {1}{2}}\mathbf {x} ^{T}{\boldsymbol {\omega }}^{-1}\mathbf {x} \right),$

where the matrix ${\boldsymbol {\omega }}$ is determined from the Lyapunov equation ${\boldsymbol {\beta }}{\boldsymbol {\omega }}+{\boldsymbol {\omega }}{\boldsymbol {\beta }}^{T}=2{\boldsymbol {D}}$ .
