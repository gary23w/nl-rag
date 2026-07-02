---
title: "Ising model (part 2/2)"
source: https://en.wikipedia.org/wiki/Ising_model
domain: computational-physics
license: CC-BY-SA-4.0
tags: computational physics, verlet integration, n-body simulation, ising model
fetched: 2026-07-02
part: 2/2
---

## Solutions

### One dimension

The thermodynamic limit exists as long as the interaction decay is $J_{ij}\sim |i-j|^{-\alpha }$ with α > 1.

- In the case of *ferromagnetic* interaction $J_{ij}\sim |i-j|^{-\alpha }$ with 1 < α < 2, Dyson proved, by comparison with the hierarchical case, that there is phase transition at small enough temperature.
- In the case of *ferromagnetic* interaction $J_{ij}\sim |i-j|^{-2}$ , Fröhlich and Spencer proved that there is phase transition at small enough temperature (in contrast with the hierarchical case).
- In the case of interaction $J_{ij}\sim |i-j|^{-\alpha }$ with α > 2 (which includes the case of finite-range interactions), there is no phase transition at any positive temperature (i.e. finite β), since the free energy is analytic in the thermodynamic parameters.
- In the case of *nearest neighbor* interactions, E. Ising provided an exact solution of the model. At any positive temperature (i.e. finite β) the free energy is analytic in the thermodynamics parameters, and the truncated two-point spin correlation decays exponentially fast. At zero temperature (i.e. infinite β), there is a second-order phase transition: the free energy is infinite, and the truncated two-point spin correlation does not decay (remains constant). Therefore, *T* = 0 is the critical temperature of this case. Scaling formulas are satisfied.

#### Ising's exact solution

In the nearest neighbor case (with periodic or free boundary conditions) an exact solution is available. The Hamiltonian of the one-dimensional Ising model on a lattice of *L* sites with free boundary conditions is $H(\sigma )=-J\sum _{i=1,\ldots ,L-1}\sigma _{i}\sigma _{i+1}-h\sum _{i}\sigma _{i},$ where *J* and *h* can be any number, since in this simplified case *J* is a constant representing the interaction strength between the nearest neighbors and *h* is the constant external magnetic field applied to lattice sites. Then the free energy is $f(\beta ,h)=-\lim _{L\to \infty }{\frac {1}{\beta L}}\ln Z(\beta )=-{\frac {1}{\beta }}\ln \left(e^{\beta J}\cosh \beta h+{\sqrt {e^{2\beta J}(\sinh \beta h)^{2}+e^{-2\beta J}}}\right),$ and the spin-spin correlation (i.e. the covariance) is $\langle \sigma _{i}\sigma _{j}\rangle -\langle \sigma _{i}\rangle \langle \sigma _{j}\rangle =C(\beta )e^{-c(\beta )|i-j|},$ where *C*(β) and *c*(β) are positive functions for *T* > 0. For *T* → 0, though, the inverse correlation length *c*(β) vanishes.

##### Proof

The proof of this result is a simple computation.

If *h* = 0, it is very easy to obtain the free energy in the case of free boundary condition, i.e. when $H(\sigma )=-J\left(\sigma _{1}\sigma _{2}+\cdots +\sigma _{L-1}\sigma _{L}\right).$ Then the model factorizes under the change of variables $\sigma '_{j}=\sigma _{j}\sigma _{j-1},\quad j\geq 2.$

This gives $Z(\beta )=\sum _{\sigma _{1},\ldots ,\sigma _{L}}e^{\beta J\sigma _{1}\sigma _{2}}e^{\beta J\sigma _{2}\sigma _{3}}\cdots e^{\beta J\sigma _{L-1}\sigma _{L}}=2\prod _{j=2}^{L}\sum _{\sigma '_{j}}e^{\beta J\sigma '_{j}}=2\left[e^{\beta J}+e^{-\beta J}\right]^{L-1}.$

Therefore, the free energy is

$f(\beta ,0)=-{\frac {1}{\beta }}\ln \left[e^{\beta J}+e^{-\beta J}\right].$

With the same change of variables

$\langle \sigma _{j}\sigma _{j+N}\rangle =\left[{\frac {e^{\beta J}-e^{-\beta J}}{e^{\beta J}+e^{-\beta J}}}\right]^{N},$

hence it decays exponentially as soon as *T* ≠ 0; but for *T* = 0, i.e. in the limit β → ∞ there is no decay.

If *h* ≠ 0 we need the transfer matrix method. For the periodic boundary conditions case is the following. The partition function is $Z(\beta )=\sum _{\sigma _{1},\ldots ,\sigma _{L}}e^{\beta h\sigma _{1}}e^{\beta J\sigma _{1}\sigma _{2}}e^{\beta h\sigma _{2}}e^{\beta J\sigma _{2}\sigma _{3}}\cdots e^{\beta h\sigma _{L}}e^{\beta J\sigma _{L}\sigma _{1}}=\sum _{\sigma _{1},\ldots ,\sigma _{L}}V_{\sigma _{1},\sigma _{2}}V_{\sigma _{2},\sigma _{3}}\cdots V_{\sigma _{L},\sigma _{1}}.$ The coefficients $V_{\sigma ,\sigma '}$ can be seen as the entries of a matrix. There are different possible choices: a convenient one (because the matrix is symmetric) is $V_{\sigma ,\sigma '}=e^{{\frac {\beta h}{2}}\sigma }e^{\beta J\sigma \sigma '}e^{{\frac {\beta h}{2}}\sigma '}$ or $V={\begin{bmatrix}e^{\beta (h+J)}&e^{-\beta J}\\e^{-\beta J}&e^{-\beta (h-J)}\end{bmatrix}}.$ In matrix formalism $Z(\beta )=\operatorname {Tr} \left(V^{L}\right)=\lambda _{1}^{L}+\lambda _{2}^{L}=\lambda _{1}^{L}\left[1+\left({\frac {\lambda _{2}}{\lambda _{1}}}\right)^{L}\right],$ where λ1 is the highest eigenvalue of *V*, while λ2 is the other eigenvalue: $\lambda _{1}=e^{\beta J}\cosh \beta h+{\sqrt {e^{2\beta J}(\cosh \beta h)^{2}-2\sinh 2\beta J}}=e^{\beta J}\cosh \beta h+{\sqrt {e^{2\beta J}(\sinh \beta h)^{2}+e^{-2\beta J}}},$ and λ2 < λ1. This gives the formula of the free energy above. In the thermodynamics limit for the non-interaction case (J = 0), we got $Z_{N}\to (\lambda _{1})^{N}=(2\cosh \beta h)^{N},$ as the answer for the open-boundary Ising model.

The energy of the lowest state is −*JL*, when all the spins are the same. For any other configuration, the extra energy is equal to 2*J* times the number of sign changes that are encountered when scanning the configuration from left to right.

If we designate the number of sign changes in a configuration as *k*, the difference in energy from the lowest energy state is 2*k*. Since the energy is additive in the number of flips, the probability *p* of having a spin-flip at each position is independent. The ratio of the probability of finding a flip to the probability of not finding one is the Boltzmann factor:

${\frac {p}{1-p}}=e^{-2\beta J}.$

The problem is reduced to independent biased coin tosses. This essentially completes the mathematical description.

From the description in terms of independent tosses, the statistics of the model for long lines can be understood. The line splits into domains. Each domain is of average length exp(2β). The length of a domain is distributed exponentially, since there is a constant probability at any step of encountering a flip. The domains never become infinite, so a long system is never magnetized. Each step reduces the correlation between a spin and its neighbor by an amount proportional to *p*, so the correlations fall off exponentially.

$\langle S_{i}S_{j}\rangle \propto e^{-p|i-j|}.$

The partition function is the volume of configurations, each configuration weighted by its Boltzmann weight. Since each configuration is described by the sign-changes, the partition function factorizes:

$Z=\sum _{\text{configs}}e^{\sum _{k}S_{k}}=\prod _{k}(1+p)=(1+p)^{L}.$

The logarithm divided by *L* is the free energy density:

$\beta f=\log(1+p)=\log \left(1+{\frac {e^{-2\beta J}}{1+e^{-2\beta J}}}\right),$

which is analytic away from β = ∞. A sign of a phase transition is a non-analytic free energy, so the one-dimensional model does not have a phase transition.

#### One-dimensional solution with transverse field

To express the Ising Hamiltonian using a quantum mechanical description of spins, we replace the spin variables with their respective Pauli matrices. However, depending on the direction of the magnetic field, we can create a transverse-field or longitudinal-field Hamiltonian. The transverse-field Hamiltonian is given by

$H(\sigma )=-J\sum _{i=1,\ldots ,L}\sigma _{i}^{z}\sigma _{i+1}^{z}-h\sum _{i}\sigma _{i}^{x}.$

The transverse-field model experiences a phase transition between an ordered and disordered regime at *J* ~ *h*. This can be shown by a mapping of Pauli matrices

$\sigma _{n}^{z}=\prod _{i=1}^{n}T_{i}^{x},$

$\sigma _{n}^{x}=T_{n}^{z}T_{n+1}^{z}.$

Upon rewriting the Hamiltonian in terms of this change-of-basis matrices, we obtain

$H(\sigma )=-h\sum _{i=1,\ldots ,L}T_{i}^{z}T_{i+1}^{z}-J\sum _{i}T_{i}^{x}.$

Since the roles of *h* and *J* are switched, the Hamiltonian undergoes a transition at *J* = *h*.

#### Renormalization

When there is no external field, we can derive a functional equation that $f(\beta ,0)=f(\beta )$ satisfies using renormalization. Specifically, let $Z_{N}(\beta ,J)$ be the partition function with N sites. Now we have: $Z_{N}(\beta ,J)=\sum _{\sigma }e^{K\sigma _{2}(\sigma _{1}+\sigma _{3})}e^{K\sigma _{4}(\sigma _{3}+\sigma _{5})}\cdots$ where $K:=\beta J$ . We sum over each of $\sigma _{2},\sigma _{4},\cdots$ , to obtain $Z_{N}(\beta ,J)=\sum _{\sigma }(2\cosh(K(\sigma _{1}+\sigma _{3})))\cdot (2\cosh(K(\sigma _{3}+\sigma _{5})))\cdots$ Now, since the cosh function is even, we can solve $Ae^{K'\sigma _{1}\sigma _{3}}=2\cosh(K(\sigma _{1}+\sigma _{3}))$ as ${\textstyle A=2{\sqrt {\cosh(2K)}},K'={\frac {1}{2}}\ln \cosh(2K)}$ . Now we have a self-similarity relation: ${\frac {1}{N}}\ln Z_{N}(K)={\frac {1}{2}}\ln \left(2{\sqrt {\cosh(2K)}}\right)+{\frac {1}{2}}{\frac {1}{N/2}}\ln Z_{N/2}(K')$ Taking the limit, we obtain $f(\beta )={\frac {1}{2}}\ln \left(2{\sqrt {\cosh(2K)}}\right)+{\frac {1}{2}}f(\beta ')$ where $\beta 'J={\frac {1}{2}}\ln \cosh(2\beta J)$ .

When $\beta$ is small, we have $f(\beta )\approx \ln 2$ , so we can numerically evaluate $f(\beta )$ by iterating the functional equation until K is small.

### Two dimensions

In the ferromagnetic case there is a phase transition. At low temperature, the Peierls argument proves positive magnetization for the nearest neighbor case and then, by the Griffiths inequality, also when longer range interactions are added. Meanwhile, at high temperature, the cluster expansion gives analyticity of the thermodynamic functions. In the nearest-neighbor case, the free energy was exactly computed by Onsager. The spin-spin correlation functions were computed by McCoy and Wu.

#### Onsager's exact solution

Onsager (1944) obtained the following analytical expression for the free energy of the Ising model on the anisotropic square lattice when the magnetic field $h=0$ in the thermodynamic limit as a function of temperature and the horizontal and vertical interaction energies $J_{1}$ and $J_{2}$ , respectively

$-\beta f=\ln 2+{\frac {1}{8\pi ^{2}}}\int _{0}^{2\pi }d\theta _{1}\int _{0}^{2\pi }d\theta _{2}\ln[\cosh(2\beta J_{1})\cosh(2\beta J_{2})-\sinh(2\beta J_{1})\cos(\theta _{1})-\sinh(2\beta J_{2})\cos(\theta _{2})].$

From this expression for the free energy, all thermodynamic functions of the model can be calculated by using an appropriate derivative. The 2D Ising model was the first model to exhibit a continuous phase transition at a positive temperature. It occurs at the temperature $T_{c}$ which solves the equation

$\sinh \left({\frac {2J_{1}}{kT_{c}}}\right)\sinh \left({\frac {2J_{2}}{kT_{c}}}\right)=1.$

In the isotropic case when the horizontal and vertical interaction energies are equal $J_{1}=J_{2}=J$ , the critical temperature $T_{c}$ occurs at the following point

$T_{c}={\frac {2J}{k\ln(1+{\sqrt {2}})}}=(2.269185\cdots ){\frac {J}{k}}$

When the interaction energies $J_{1}$ , $J_{2}$ are both negative, the Ising model becomes an antiferromagnet. Since the square lattice is bi-partite, it is invariant under this change when the magnetic field $h=0$ , so the free energy and critical temperature are the same for the antiferromagnetic case. For the triangular lattice, which is not bi-partite, the ferromagnetic and antiferromagnetic Ising model behave notably differently. Specifically, around a triangle, it is impossible to make all 3 spin-pairs antiparallel, so the antiferromagnetic Ising model cannot reach the minimal energy state. This is an example of geometric frustration.

##### Onsager's formula for spontaneous magnetization

Onsager famously announced the following expression for the spontaneous magnetization *M* of a two-dimensional Ising ferromagnet on the square lattice at two different conferences in 1948, though without proof

$M=\left(1-\left[\sinh 2\beta J_{1}\sinh 2\beta J_{2}\right]^{-2}\right)^{\frac {1}{8}}$

where $J_{1}$ and $J_{2}$ are horizontal and vertical interaction energies.

A complete derivation was only given in 1951 by Yang (1952) using a limiting process of transfer matrix eigenvalues. The proof was subsequently greatly simplified in 1963 by Montroll, Potts, and Ward using Szegő's limit formula for Toeplitz determinants by treating the magnetization as the limit of correlation functions.

#### Minimal model

At the critical point, the two-dimensional Ising model is a two-dimensional conformal field theory. The spin and energy correlation functions are described by a minimal model, which has been exactly solved.

### Three dimensions

In three as in two dimensions, the most studied case of the Ising model is the translation-invariant model on a cubic lattice with nearest-neighbor coupling in the zero magnetic field. Many theoreticians searched for an analytical three-dimensional solution for many decades, which would be analogous to Onsager's solution in the two-dimensional case. Such a solution has not been found until now, although there is no proof that it may not exist. In three dimensions, the Ising model was shown to have a representation in terms of non-interacting fermionic strings by Alexander Polyakov and Vladimir Dotsenko. This construction has been carried on the lattice, and the continuum limit, conjecturally describing the critical point, is unknown.

In three as in two dimensions, Peierls' argument shows that there is a phase transition. This phase transition is rigorously known to be continuous (in the sense that correlation length diverges and the magnetization goes to zero), and is called the critical point. It is believed that the critical point can be described by a renormalization group fixed point of the Wilson-Kadanoff renormalization group transformation. It is also believed that the phase transition can be described by a three-dimensional unitary conformal field theory, as evidenced by Monte Carlo simulations, exact diagonalization results in quantum models, and quantum field theoretical arguments. Although it is an open problem to establish rigorously the renormalization group picture or the conformal field theory picture, theoretical physicists have used these two methods to compute the critical exponents of the phase transition, which agree with the experiments and with the Monte Carlo simulations. This conformal field theory describing the three-dimensional Ising critical point is under active investigation using the method of the conformal bootstrap. This method currently yields the most precise information about the structure of the critical theory (see Ising critical exponents).

In 2000, Sorin Istrail of Sandia National Laboratories proved that the spin glass Ising model on a nonplanar lattice is NP-complete. That is, assuming **P** ≠ **NP,** the general spin glass Ising model is exactly solvable only in planar cases, so solutions for dimensions higher than two are also intractable. Istrail's result only concerns the spin glass model with spatially varying couplings, and tells nothing about Ising's original ferromagnetic model with equal couplings.

### Four dimensions and above

In any dimension, the Ising model can be productively described by a locally varying mean field. The field is defined as the average spin value over a large region, but not so large so as to include the entire system. The field still has slow variations from point to point, as the averaging volume moves. These fluctuations in the field are described by a continuum field theory in the infinite system limit. The accuracy of this approximation improves as the dimension becomes larger. A deeper understanding of how the Ising model behaves, going beyond mean-field approximations, can be achieved using renormalization group methods.
