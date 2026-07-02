---
title: "Mean-field theory"
source: https://en.wikipedia.org/wiki/Mean_field_theory
domain: variational-bayes
license: CC-BY-SA-4.0
tags: variational Bayesian methods, evidence lower bound, Kullback Leibler divergence, mean field
fetched: 2026-07-02
---

# Mean-field theory

(Redirected from

Mean field theory

)

In physics and probability theory, **mean-field theory** (**MFT**) or **self-consistent field theory** studies the behavior of high-dimensional random (stochastic) models by studying a simpler model that approximates the original by averaging over degrees of freedom (the number of values in the final calculation of a statistic that are free to vary). Such models consider many individual components that interact with each other.

The main idea of MFT is to replace all interactions to any one body with an average or effective interaction, sometimes called a *molecular field*. This reduces any many-body problem into an effective one-body problem. The ease of solving MFT problems means that some insight into the behavior of the system can be obtained at a lower computational cost.

MFT has since been applied to a wide range of fields outside of physics, including statistical inference, graphical models, neuroscience, artificial intelligence, epidemic models, queueing theory, computer-network performance and game theory, as in the quantal response equilibrium.

## Origins

The idea first appeared in physics (statistical mechanics) in the work of Pierre Curie and Pierre Weiss to describe phase transitions. MFT has been used in the Bragg–Williams approximation, models on Bethe lattice, Landau theory, Curie-Weiss law for magnetic susceptibility, Flory–Huggins solution theory, and Scheutjens–Fleer theory.

Systems with many (sometimes infinite) degrees of freedom are generally hard to solve exactly or compute in closed, analytic form, except for some simple cases (e.g. certain Gaussian random-field theories, the 1D Ising model). Often combinatorial problems arise that make things like computing the partition function of a system difficult. MFT is an approximation method that often makes the original problem to be solvable and open to calculation, and in some cases MFT may give very accurate approximations.

In field theory, the Hamiltonian may be expanded in terms of the magnitude of fluctuations around the mean of the field. In this context, MFT can be viewed as the "zeroth-order" expansion of the Hamiltonian in fluctuations. Physically, this means that an MFT system has no fluctuations, but this coincides with the idea that one is replacing all interactions with a "mean-field”.

Quite often, MFT provides a convenient launch point for studying higher-order fluctuations. For example, when computing the partition function, studying the combinatorics of the interaction terms in the Hamiltonian can sometimes at best produce perturbation results or Feynman diagrams that correct the mean-field approximation.

## Validity

In general, dimensionality plays an active role in determining whether a mean-field approach will work for any particular problem. There is sometimes a critical dimension above which MFT is valid and below which it is not.

Heuristically, many interactions are replaced in MFT by one effective interaction. So if the field or particle exhibits many random interactions in the original system, they tend to cancel each other out, so the mean effective interaction and MFT will be more accurate. This is true in cases of high dimensionality, when the Hamiltonian includes long-range forces, or when the particles are extended (e.g. polymers). The Ginzburg criterion is the formal expression of how fluctuations render MFT a poor approximation, often depending upon the number of spatial dimensions in the system of interest.

## Formal approach (Hamiltonian)

The formal basis for mean-field theory is the Bogoliubov inequality. This inequality states that the free energy of a system with Hamiltonian

${\mathcal {H}}={\mathcal {H}}_{0}+\Delta {\mathcal {H}}$

has the following upper bound:

$F\leq F_{0}\ {\stackrel {\mathrm {def} }{=}}\ \langle {\mathcal {H}}\rangle _{0}-TS_{0},$

where $S_{0}$ is the entropy, and F and $F_{0}$ are Helmholtz free energies. The average is taken over the equilibrium ensemble of the reference system with Hamiltonian ${\mathcal {H}}_{0}$ . In the special case that the reference Hamiltonian is that of a non-interacting system and can thus be written as

${\mathcal {H}}_{0}=\sum _{i=1}^{N}h_{i}(\xi _{i}),$

where $\xi _{i}$ are the degrees of freedom of the individual components of our statistical system (atoms, spins and so forth), one can consider sharpening the upper bound by minimising the right side of the inequality. The minimising reference system is then the "best" approximation to the true system using non-correlated degrees of freedom and is known as the **mean field approximation**.

For the most common case that the target Hamiltonian contains only pairwise interactions, i.e.,

${\mathcal {H}}=\sum _{(i,j)\in {\mathcal {P}}}V_{i,j}(\xi _{i},\xi _{j}),$

where ${\mathcal {P}}$ is the set of pairs that interact, the minimising procedure can be carried out formally. Define $\operatorname {Tr} _{i}f(\xi _{i})$ as the generalized sum of the observable f over the degrees of freedom of the single component (sum for discrete variables, integrals for continuous ones). The approximating free energy is given by

${\begin{aligned}F_{0}&=\operatorname {Tr} _{1,2,\ldots ,N}{\mathcal {H}}(\xi _{1},\xi _{2},\ldots ,\xi _{N})P_{0}^{(N)}(\xi _{1},\xi _{2},\ldots ,\xi _{N})\\&+kT\,\operatorname {Tr} _{1,2,\ldots ,N}P_{0}^{(N)}(\xi _{1},\xi _{2},\ldots ,\xi _{N})\log P_{0}^{(N)}(\xi _{1},\xi _{2},\ldots ,\xi _{N}),\end{aligned}}$

where $P_{0}^{(N)}(\xi _{1},\xi _{2},\dots ,\xi _{N})$ is the probability to find the reference system in the state specified by the variables $(\xi _{1},\xi _{2},\dots ,\xi _{N})$ . This probability is given by the normalized Boltzmann factor

${\begin{aligned}P_{0}^{(N)}(\xi _{1},\xi _{2},\ldots ,\xi _{N})&={\frac {1}{Z_{0}^{(N)}}}e^{-\beta {\mathcal {H}}_{0}(\xi _{1},\xi _{2},\ldots ,\xi _{N})}\\&=\prod _{i=1}^{N}{\frac {1}{Z_{0}}}e^{-\beta h_{i}(\xi _{i})}\ {\stackrel {\mathrm {def} }{=}}\ \prod _{i=1}^{N}P_{0}^{(i)}(\xi _{i}),\end{aligned}}$

where $Z_{0}$ is the partition function. Thus

${\begin{aligned}F_{0}&=\sum _{(i,j)\in {\mathcal {P}}}\operatorname {Tr} _{i,j}V_{i,j}(\xi _{i},\xi _{j})P_{0}^{(i)}(\xi _{i})P_{0}^{(j)}(\xi _{j})\\&+kT\sum _{i=1}^{N}\operatorname {Tr} _{i}P_{0}^{(i)}(\xi _{i})\log P_{0}^{(i)}(\xi _{i}).\end{aligned}}$

In order to minimise, we take the derivative with respect to the single-degree-of-freedom probabilities $P_{0}^{(i)}$ using a Lagrange multiplier to ensure proper normalization. The end result is the set of self-consistency equations

$P_{0}^{(i)}(\xi _{i})={\frac {1}{Z_{0}}}e^{-\beta h_{i}^{MF}(\xi _{i})},\quad i=1,2,\ldots ,N,$

where the mean field is given by

$h_{i}^{\text{MF}}(\xi _{i})=\sum _{\{j\mid (i,j)\in {\mathcal {P}}\}}\operatorname {Tr} _{j}V_{i,j}(\xi _{i},\xi _{j})P_{0}^{(j)}(\xi _{j}).$

## Applications

Mean field theory can be applied to a number of physical systems so as to study phenomena such as phase transitions.

### Ising model

#### Formal derivation

The Bogoliubov inequality, shown above, can be used to find the dynamics of a mean field model of the two-dimensional Ising lattice. A magnetisation function can be calculated from the resultant approximate free energy. The first step is choosing a more tractable approximation of the true Hamiltonian. Using a non-interacting or effective field Hamiltonian,

$-m\sum _{i}s_{i}$

,

the variational free energy is

$F_{V}=F_{0}+\left\langle \left(-J\sum s_{i}s_{j}-h\sum s_{i}\right)-\left(-m\sum s_{i}\right)\right\rangle _{0}.$

By the Bogoliubov inequality, simplifying this quantity and calculating the magnetisation function that minimises the variational free energy yields the best approximation to the actual magnetisation. The minimiser is

$m=J\sum \langle s_{j}\rangle _{0}+h,$

which is the ensemble average of spin. This simplifies to

$m={\text{tanh}}(zJ\beta m+h$

).

Equating the effective field felt by all spins to a mean spin value relates the variational approach to the suppression of fluctuations. The physical interpretation of the magnetisation function is then a field of mean values for individual spins.

#### Non-interacting spins approximation

Consider the Ising model on a d -dimensional lattice. The Hamiltonian is given by

$H=-J\sum _{\langle i,j\rangle }s_{i}s_{j}-h\sum _{i}s_{i},$

where the $\sum _{\langle i,j\rangle }$ indicates summation over the pair of nearest neighbors $\langle i,j\rangle$ , and $s_{i},s_{j}=\pm 1$ are neighboring Ising spins.

Let us transform our spin variable by introducing the fluctuation from its mean value $m_{i}\equiv \langle s_{i}\rangle$ . We may rewrite the Hamiltonian as

$H=-J\sum _{\langle i,j\rangle }(m_{i}+\delta s_{i})(m_{j}+\delta s_{j})-h\sum _{i}s_{i},$

where we define $\delta s_{i}\equiv s_{i}-m_{i}$ ; this is the *fluctuation* of the spin.

If we expand the right side, we obtain one term that is entirely dependent on the mean values of the spins and independent of the spin configurations. This is the trivial term, which does not affect the statistical properties of the system. The next term is the one involving the product of the mean value of the spin and the fluctuation value. Finally, the last term involves a product of two fluctuation values.

The mean field approximation consists of neglecting this second-order fluctuation term:

$H\approx H^{\text{MF}}\equiv -J\sum _{\langle i,j\rangle }(m_{i}m_{j}+m_{i}\delta s_{j}+m_{j}\delta s_{i})-h\sum _{i}s_{i}.$

These fluctuations are enhanced at low dimensions, making MFT a better approximation for high dimensions.

Again, the summand can be re-expanded. In addition, we expect that the mean value of each spin is site-independent, since the Ising chain is translationally invariant. This yields

$H^{\text{MF}}=-J\sum _{\langle i,j\rangle }{\big (}m^{2}+2m(s_{i}-m){\big )}-h\sum _{i}s_{i}.$

The summation over neighboring spins can be rewritten as $\sum _{\langle i,j\rangle }={\frac {1}{2}}\sum _{i}\sum _{j\in nn(i)}$ , where $nn(i)$ means "nearest neighbor of i ", and the $1/2$ prefactor avoids double counting, since each bond participates in two spins. Simplifying leads to the final expression

$H^{\text{MF}}={\frac {Jm^{2}Nz}{2}}-\underbrace {(h+mJz)} _{h^{\text{eff.}}}\sum _{i}s_{i},$

where z is the coordination number. At this point, the Ising Hamiltonian has been *decoupled* into a sum of one-body Hamiltonians with an *effective mean field* $h^{\text{eff.}}=h+Jzm$ , which is the sum of the external field h and of the *mean field* induced by the neighboring spins. It is worth noting that this mean field directly depends on the number of nearest neighbors and thus on the dimension of the system (for instance, for a hypercubic lattice of dimension d , $z=2d$ ).

Substituting this Hamiltonian into the partition function and solving the effective 1D problem, we obtain

$Z=e^{-{\frac {\beta Jm^{2}Nz}{2}}}\left[2\cosh \left({\frac {h+mJz}{k_{\text{B}}T}}\right)\right]^{N},$

where N is the number of lattice sites. This is a closed and exact expression for the partition function of the system. We may obtain the free energy of the system and calculate critical exponents. In particular, we can obtain the magnetization m as a function of $h^{\text{eff.}}$ .

We thus have two equations between m and $h^{\text{eff.}}$ , allowing us to determine m as a function of temperature. This leads to the following observation:

- For temperatures greater than a certain value $T_{\text{c}}$ , the only solution is $m=0$ . The system is paramagnetic.
- For $T<T_{\text{c}}$ , there are two non-zero solutions: $m=\pm m_{0}$ . The system is ferromagnetic.

$T_{\text{c}}$ is given by the following relation: $T_{\text{c}}={\frac {Jz}{k_{B}}}$ .

This shows that MFT can account for the ferromagnetic phase transition.

### Application to other systems

Similarly, MFT can be applied to other types of Hamiltonian as in the following cases:

- To study the metal–superconductor transition. In this case, the analog of the magnetization is the superconducting gap $\Delta$ .
- The molecular field of a liquid crystal that emerges when the Laplacian of the director field is non-zero.
- To determine the optimal amino acid side chain packing given a fixed protein backbone in protein structure prediction (see Self-consistent mean field (biology)).
- To determine the elastic properties of a composite material.

Variationally minimisation like mean field theory can be also be used in statistical inference.

## Extension to time-dependent mean fields

In mean field theory, the mean field appearing in the single-site problem is a time-independent scalar or vector quantity. However, this isn't always the case: in a variant of mean field theory called dynamical mean field theory (DMFT), the mean field becomes a time-dependent quantity. For instance, DMFT can be applied to the Hubbard model to study the metal–Mott-insulator transition.
