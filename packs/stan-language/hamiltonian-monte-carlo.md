---
title: "Hamiltonian Monte Carlo"
source: https://en.wikipedia.org/wiki/Hamiltonian_Monte_Carlo
domain: stan-language
license: CC-BY-SA-4.0
tags: stan language, statistical modeling language, hamiltonian monte carlo, bayesian estimation
fetched: 2026-07-02
---

# Hamiltonian Monte Carlo

The **Hamiltonian Monte Carlo** algorithm (originally known as **hybrid Monte Carlo**) is a Markov chain Monte Carlo method for obtaining a sequence of random samples whose distribution converges to a target probability distribution that is difficult to sample directly. This sequence can be used to estimate integrals of the target distribution, such as expected values and moments.

Hamiltonian Monte Carlo corresponds to an instance of the Metropolis–Hastings algorithm, with a Hamiltonian dynamics evolution simulated using a time-reversible and volume-preserving numerical integrator (typically the leapfrog integrator) to propose a move to a new point in the state space. Compared to using a Gaussian random walk proposal distribution in the Metropolis–Hastings algorithm, Hamiltonian Monte Carlo reduces the correlation between successive sampled states by proposing moves to distant states which maintain a high probability of acceptance due to the approximate energy conserving properties of the simulated Hamiltonian dynamic when using a symplectic integrator. The reduced correlation means fewer Markov chain samples are needed to approximate integrals with respect to the target probability distribution for a given Monte Carlo error.

The algorithm was originally proposed by Simon Duane, Anthony Kennedy, Brian Pendleton and Duncan Roweth in 1987 for calculations in lattice quantum chromodynamics. In 1996, Radford M. Neal showed how the method could be used for a broader class of statistical problems, in particular artificial neural networks. But the burden of having to provide the algorithm with gradients of the model graph delayed its wider adoption in statistics and other quantitative disciplines, until in the mid-2010s the developers of Stan implemented HMC in combination with automatic differentiation.

## Algorithm

Suppose the target distribution to sample is $f(\mathbf {x} )$ for $\mathbf {x} \in \mathbb {R} ^{d}$ ( $d\geq 1$ ) and a chain of samples $\mathbf {X} _{0},\mathbf {X} _{1},\mathbf {X} _{2},\ldots$ is required.

Hamilton's equations are

${\frac {{\text{d}}x_{i}}{{\text{d}}t}}={\frac {\partial H}{\partial p_{i}}}\quad {\text{and}}\quad {\dfrac {{\text{d}}p_{i}}{{\text{d}}t}}=-{\dfrac {\partial H}{\partial x_{i}}}$

where $x_{i}$ and $p_{i}$ are the i th component of the position and momentum vector respectively and H is the Hamiltonian. Let M be a mass matrix which is symmetric and positive definite, then the Hamiltonian is

$H(\mathbf {x} ,\mathbf {p} )=U(\mathbf {x} )+{\dfrac {1}{2}}\mathbf {p} ^{\text{T}}M^{-1}\mathbf {p}$

where $U(\mathbf {x} )$ is the potential energy. The potential energy for a target is given as

$U(\mathbf {x} )=-\ln f(\mathbf {x} )$

which comes from the Boltzmann's factor. Note that the Hamiltonian H is dimensionless in this formulation because the exponential probability weight $\exp \left(-H\right)$ has to be well defined. For example, in simulations at finite temperature T the factor $k_{\text{B}}T$ (with the Boltzmann constant $k_{\text{B}}$ ) is directly absorbed into U and M .

The algorithm requires a positive integer for number of leapfrog steps L and a positive number for the step size $\Delta t$ . Suppose the chain is at $\mathbf {X} _{n}=\mathbf {x} _{n}$ . Let $\mathbf {x} _{n}(0)=\mathbf {x} _{n}$ . First, a random Gaussian momentum $\mathbf {p} _{n}(0)$ is drawn from ${\text{N}}\left(\mathbf {0} ,M\right)$ . Next, the particle will run under Hamiltonian dynamics for time $L\Delta t$ , this is done by solving the Hamilton's equations numerically using the leapfrog algorithm. The position and momentum vectors after time $\Delta t$ using the leapfrog algorithm are:

$\mathbf {p} _{n}\left(t+{\dfrac {\Delta t}{2}}\right)=\mathbf {p} _{n}(t)-{\dfrac {\Delta t}{2}}\nabla \left.U(\mathbf {x} )\right|_{\mathbf {x} =\mathbf {x} _{n}(t)}$

$\mathbf {x} _{n}(t+\Delta t)=\mathbf {x} _{n}(t)+\Delta tM^{-1}\mathbf {p} _{n}\left(t+{\dfrac {\Delta t}{2}}\right)$

$\mathbf {p} _{n}(t+\Delta t)=\mathbf {p} _{n}\left(t+{\dfrac {\Delta t}{2}}\right)-{\dfrac {\Delta t}{2}}\nabla \left.U(\mathbf {x} )\right|_{\mathbf {x} =\mathbf {x} _{n}(t+\Delta t)}$

These equations are to be applied to $\mathbf {x} _{n}(0)$ and $\mathbf {p} _{n}(0)$ L times to obtain $\mathbf {x} _{n}(L\Delta t)$ and $\mathbf {p} _{n}(L\Delta t)$ .

The leapfrog algorithm is an approximate solution to the motion of non-interacting classical particles. If exact, the solution will never change the initial randomly-generated energy distribution, as energy is conserved for each particle in the presence of a classical potential energy field. In order to reach a thermodynamic equilibrium distribution, particles must have some sort of interaction with, for example, a surrounding heat bath, so that the entire system can take on different energies with probabilities according to the Boltzmann distribution.

One way to move the system towards a thermodynamic equilibrium distribution is to change the state of the particles using the Metropolis–Hastings algorithm. So first, one applies the leapfrog step, then a Metropolis-Hastings step.

The transition from $\mathbf {X} _{n}=\mathbf {x} _{n}$ to $\mathbf {X} _{n+1}$ is

$\mathbf {X} _{n+1}|\mathbf {X} _{n}=\mathbf {x} _{n}={\begin{cases}\mathbf {x} _{n}(L\Delta t)&{\text{with probability }}\alpha \left(\mathbf {x} _{n}(0),\mathbf {x} _{n}(L\Delta t)\right)\\\mathbf {x} _{n}(0)&{\text{otherwise}}\end{cases}}$

where

$\alpha \left(\mathbf {x} _{n}(0),\mathbf {x} _{n}(L\Delta t)\right)={\text{min}}\left(1,{\dfrac {\exp \left[-H(\mathbf {x} _{n}(L\Delta t),\mathbf {p} _{n}(L\Delta t))\right]}{\exp \left[-H(\mathbf {x} _{n}(0),\mathbf {p} _{n}(0))\right]}}\right).$

A full update consists of first randomly sampling the momenta $\mathbf {p}$ (independently of the previous iterations), then integrating the equations of motion (e.g. with leapfrog), and finally obtaining the new configuration from the Metropolis-Hastings accept/reject step. This updating mechanism is repeated to obtain $\mathbf {X} _{n+1},\mathbf {X} _{n+2},\mathbf {X} _{n+3},\ldots$ .

## No U-Turn Sampler

The No U-Turn Sampler (NUTS) is an extension by controlling the number of steps L automatically. Tuning L is critical. For example, in the one dimensional ${\text{N}}(0,1/{\sqrt {k}})$ case, the potential is $U(x)=kx^{2}/2$ which corresponds to the potential of a simple harmonic oscillator. For L too large, the particle will oscillate and thus waste computational time. For L too small, the particle will behave like a random walk.

Loosely, NUTS runs the Hamiltonian dynamics both forwards and backwards in time randomly until a U-Turn condition is satisfied. When that happens, a random point from the path is chosen for the MCMC sample and the process is repeated from that new point.

In detail, a binary tree is constructed to trace the path of the leap frog steps. To produce a MCMC sample, an iterative procedure is conducted. A slice variable $U_{n}\sim {\text{Uniform}}(0,\exp(-H[\mathbf {x} _{n}(0),\mathbf {p} _{n}(0)]))$ is sampled. Let $\mathbf {x} _{n}^{+}$ and $\mathbf {p} _{n}^{+}$ be the position and momentum of the forward particle respectively. Similarly, $\mathbf {x} _{n}^{-}$ and $\mathbf {p} _{n}^{-}$ for the backward particle. In each iteration, the binary tree selects at random uniformly to move the forward particle forwards in time or the backward particle backwards in time. Also for each iteration, the number of leap frog steps increase by a factor of 2. For example, in the first iteration, the forward particle moves forwards in time using 1 leap frog step. In the next iteration, the backward particle moves backwards in time using 2 leap frog steps.

The iterative procedure continues until the U-Turn condition is met, that is

$(\mathbf {x} _{n}^{+}-\mathbf {x} _{n}^{-})\cdot \mathbf {p} _{n}^{-}<0\quad {\text{or}}\quad .(\mathbf {x} _{n}^{+}-\mathbf {x} _{n}^{-})\cdot \mathbf {p} _{n}^{+}<0$

or when the Hamiltonian becomes inaccurate

$\exp \left[-H(\mathbf {x} _{n}^{+},\mathbf {p} _{n}^{+})+\delta \right]<U_{n}$

or

$\exp \left[-H(\mathbf {x} _{n}^{-},\mathbf {p} _{n}^{-})+\delta \right]<U_{n}$

where, for example, $\delta =1000$ .

Once the U-Turn condition is met, the next MCMC sample, $\mathbf {x} _{n+1}$ , is obtained by sampling uniformly the leap frog path traced out by the binary tree $\{\mathbf {x} _{n}^{-},\ldots ,\mathbf {x} _{n}(-\Delta t),\mathbf {x} _{n}(0),\mathbf {x} _{n}(\Delta t),\ldots ,\mathbf {x} _{n}^{+}\}$ which satisfies

$U_{n}<\exp \left[-H(\mathbf {x_{n+1}} ,\mathbf {p_{n+1})} \right]$

.

This is usually satisfied if the remaining HMC parameters are sensible.
