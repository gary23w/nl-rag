---
title: "Perturbation theory (quantum mechanics) (part 2/2)"
source: https://en.wikipedia.org/wiki/Perturbation_theory_(quantum_mechanics)
domain: perturbation-theory
license: CC-BY-SA-4.0
tags: perturbation theory, method of averaging, multiple-scale analysis, adiabatic theorem
fetched: 2026-07-02
part: 2/2
---

## Time-dependent perturbation theory

### Method of variation of constants

Time-dependent perturbation theory, initiated by Paul Dirac and further developed by John Archibald Wheeler, Richard Feynman, and Freeman Dyson, studies the effect of a time-dependent perturbation *V*(*t*) applied to a time-independent Hamiltonian *H*0. It is an extremely valuable tool for calculating the properties of any physical system. It is used for the quantitative description of phenomena as diverse as proton-proton scattering, photo-ionization of materials, scattering of electrons off lattice defects in a conductor, scattering of neutrons off nuclei, electric susceptibilities of materials, neutron absorption cross sections in a nuclear reactor, and much more.

Since the perturbed Hamiltonian is time-dependent, so are its energy levels and eigenstates. Thus, the goals of time-dependent perturbation theory are slightly different from time-independent perturbation theory. One is interested in the following quantities:

- The time-dependent expectation value of some observable A, for a given initial state.
- The time-dependent expansion coefficients (w.r.t. a given time-dependent state) of those basis states that are energy eigenkets (eigenvectors) in the unperturbed system.

The first quantity is important because it gives rise to the classical result of an A measurement performed on a macroscopic number of copies of the perturbed system. For example, we could take A to be the displacement in the x-direction of the electron in a hydrogen atom, in which case the expected value, when multiplied by an appropriate coefficient, gives the time-dependent dielectric polarization of a hydrogen gas. With an appropriate choice of perturbation (i.e. an oscillating electric potential), this allows one to calculate the AC permittivity of the gas.

The second quantity looks at the time-dependent probability of occupation for each eigenstate. This is particularly useful in laser physics, where one is interested in the populations of different atomic states in a gas when a time-dependent electric field is applied. These probabilities are also useful for calculating the "quantum broadening" of spectral lines (see line broadening) and particle decay in particle physics and nuclear physics.

We will briefly examine the method behind Dirac's formulation of time-dependent perturbation theory. Choose an energy basis ${|n\rangle }$ for the unperturbed system. (We drop the (0) superscripts for the eigenstates, because it is not useful to speak of energy levels and eigenstates for the perturbed system.)

If the unperturbed system is an eigenstate (of the Hamiltonian) $|j\rangle$ at time t = 0, its state at subsequent times varies only by a phase (in the Schrödinger picture, where state vectors evolve in time and operators are constant), $|j(t)\rangle =e^{-iE_{j}t/\hbar }|j\rangle ~.$

Now, introduce a time-dependent perturbing Hamiltonian *V*(*t*). The Hamiltonian of the perturbed system is $H=H_{0}+V(t)~.$ Let $|\psi (t)\rangle$ denote the quantum state of the perturbed system at time t. It obeys the time-dependent Schrödinger equation, $H|\psi (t)\rangle =i\hbar {\frac {\partial }{\partial t}}|\psi (t)\rangle ~.$

The quantum state at each instant can be expressed as a linear combination of the complete eigenbasis of $|n\rangle$ :

| $\|\psi (t)\rangle =\sum _{n}c_{n}(t)e^{-iE_{n}t/\hbar }\|n\rangle ~,$ |   | 1 |
|---|---|---|

where the *cn*(*t*)s are to be determined complex functions of t which we will refer to as **amplitudes** (strictly speaking, they are the amplitudes in the Dirac picture).

We have explicitly extracted the exponential phase factors $\exp(-iE_{n}t/\hbar )$ on the right hand side. This is only a matter of convention, and may be done without loss of generality. The reason we go to this trouble is that when the system starts in the state $|j\rangle$ and no perturbation is present, the amplitudes have the convenient property that, for all t, *cj*(*t*) = 1 and *cn*(*t*) = 0 if *n ≠ j*.

The square of the absolute amplitude *cn*(*t*) is the probability that the system is in state n at time t, since $\left|c_{n}(t)\right|^{2}=\left|\langle n|\psi (t)\rangle \right|^{2}~.$

Plugging into the Schrödinger equation and using the fact that ∂/∂*t* acts by a product rule, one obtains $\sum _{n}\left(i\hbar {\frac {dc_{n}}{dt}}-c_{n}(t)V(t)\right)e^{-iE_{n}t/\hbar }|n\rangle =0~.$

By resolving the identity in front of V and multiplying through by the bra $\langle n|$ on the left, this can be reduced to a set of coupled differential equations for the amplitudes, ${\frac {dc_{n}}{dt}}={\frac {-i}{\hbar }}\sum _{k}\langle n|V(t)|k\rangle \,c_{k}(t)\,e^{-i(E_{k}-E_{n})t/\hbar }~.$

where we have used equation (**1**) to evaluate the sum on n in the second term, then used the fact that $\langle k|\Psi (t)\rangle =c_{k}(t)e^{-iE_{k}t/\hbar }$ .

The matrix elements of V play a similar role as in time-independent perturbation theory, being proportional to the rate at which amplitudes are shifted between states. Note, however, that the direction of the shift is modified by the exponential phase factor. Over times much longer than the energy difference *Ek* − *En*, the phase winds around 0 several times. If the time-dependence of V is sufficiently slow, this may cause the state amplitudes to oscillate. (For example, such oscillations are useful for managing radiative transitions in a laser.)

Up to this point, we have made no approximations, so this set of differential equations is exact. By supplying appropriate initial values *cn*(*t*), we could in principle find an exact (i.e., non-perturbative) solution. This is easily done when there are only two energy levels (n = 1, 2), and this solution is useful for modelling systems like the ammonia molecule.

However, exact solutions are difficult to find when there are many energy levels, and one instead looks for perturbative solutions. These may be obtained by expressing the equations in an integral form, $c_{n}(t)=c_{n}(0)-{\frac {i}{\hbar }}\sum _{k}\int _{0}^{t}dt'\;\langle n|V(t')|k\rangle \,c_{k}(t')\,e^{-i(E_{k}-E_{n})t'/\hbar }~.$

Repeatedly substituting this expression for cn back into right hand side, yields an iterative solution, $c_{n}(t)=c_{n}^{(0)}+c_{n}^{(1)}+c_{n}^{(2)}+\cdots$ where, for example, the first-order term is $c_{n}^{(1)}(t)={\frac {-i}{\hbar }}\sum _{k}\int _{0}^{t}dt'\;\langle n|V(t')|k\rangle \,c_{k}^{(0)}\,e^{-i(E_{k}-E_{n})t'/\hbar }~.$ To the same approximation, the summation in the above expression can be removed since in the unperturbed state $c_{k}^{(0)}=\delta _{kn}$ so that we have $c_{n}^{(1)}(t)={\frac {-i}{\hbar }}\int _{0}^{t}dt'\;\langle n|V(t')|k\rangle \,e^{-i(E_{k}-E_{n})t'/\hbar }~.$

Several further results follow from this, such as Fermi's golden rule, which relates the rate of transitions between quantum states to the density of states at particular energies; or the Dyson series, obtained by applying the iterative method to the time evolution operator, which is one of the starting points for the method of Feynman diagrams.

### Method of Dyson series

Time-dependent perturbations can be reorganized through the technique of the Dyson series. The Schrödinger equation $H(t)|\psi (t)\rangle =i\hbar {\frac {\partial |\psi (t)\rangle }{\partial t}}$ has the formal solution $|\psi (t)\rangle =T\exp {\left[-{\frac {i}{\hbar }}\int _{t_{0}}^{t}dt'H(t')\right]}|\psi (t_{0})\rangle ~,$ where T is the time ordering operator, $TA(t_{1})A(t_{2})={\begin{cases}A(t_{1})A(t_{2})&t_{1}>t_{2}\\A(t_{2})A(t_{1})&t_{2}>t_{1}\end{cases}}~.$ Thus, the exponential represents the following Dyson series, $|\psi (t)\rangle =\left[1-{\frac {i}{\hbar }}\int _{t_{0}}^{t}dt_{1}H(t_{1})-{\frac {1}{\hbar ^{2}}}\int _{t_{0}}^{t}dt_{1}\int _{t_{0}}^{t_{1}}dt_{2}H(t_{1})H(t_{2})+\ldots \right]|\psi (t_{0})\rangle ~.$ Note that in the second term, the 1/2! factor exactly cancels the double contribution due to the time-ordering operator, etc.

Consider the following perturbation problem $[H_{0}+\lambda V(t)]|\psi (t)\rangle =i\hbar {\frac {\partial |\psi (t)\rangle }{\partial t}}~,$ assuming that the parameter λ is small and that the problem $H_{0}|n\rangle =E_{n}|n\rangle$ has been solved.

Perform the following unitary transformation to the interaction picture (or Dirac picture), $|\psi (t)\rangle =e^{-{\frac {i}{\hbar }}H_{0}(t-t_{0})}|\psi _{I}(t)\rangle ~.$ Consequently, the Schrödinger equation simplifies to $\lambda e^{{\frac {i}{\hbar }}H_{0}(t-t_{0})}V(t)e^{-{\frac {i}{\hbar }}H_{0}(t-t_{0})}|\psi _{I}(t)\rangle =i\hbar {\frac {\partial |\psi _{I}(t)\rangle }{\partial t}}~,$ so it is solved through the above Dyson series, $|\psi _{I}(t)\rangle =\left[1-{\frac {i\lambda }{\hbar }}\int _{t_{0}}^{t}dt_{1}e^{{\frac {i}{\hbar }}H_{0}(t_{1}-t_{0})}V(t_{1})e^{-{\frac {i}{\hbar }}H_{0}(t_{1}-t_{0})}-{\frac {\lambda ^{2}}{\hbar ^{2}}}\int _{t_{0}}^{t}dt_{1}\int _{t_{0}}^{t_{1}}dt_{2}e^{{\frac {i}{\hbar }}H_{0}(t_{1}-t_{0})}V(t_{1})e^{-{\frac {i}{\hbar }}H_{0}(t_{1}-t_{0})}e^{{\frac {i}{\hbar }}H_{0}(t_{2}-t_{0})}V(t_{2})e^{-{\frac {i}{\hbar }}H_{0}(t_{2}-t_{0})}+\ldots \right]|\psi (t_{0})\rangle ~,$ as a perturbation series with small λ.

Using the solution of the unperturbed problem $H_{0}|n\rangle =E_{n}|n\rangle$ and $\sum _{n}|n\rangle \langle n|=1$ (for the sake of simplicity assume a pure discrete spectrum), yields, to first order, $|\psi _{I}(t)\rangle =\left[1-{\frac {i\lambda }{\hbar }}\sum _{m}\sum _{n}\int _{t_{0}}^{t}dt_{1}\langle m|V(t_{1})|n\rangle e^{-{\frac {i}{\hbar }}(E_{n}-E_{m})(t_{1}-t_{0})}|m\rangle \langle n|+\ldots \right]|\psi (t_{0})\rangle ~.$

Thus, the system, initially in the unperturbed state $|\alpha \rangle =|\psi (t_{0})\rangle$ , by dint of the perturbation can go into the state $|\beta \rangle$ . The corresponding transition probability amplitude to first order is $A_{\alpha \beta }=-{\frac {i\lambda }{\hbar }}\int _{t_{0}}^{t}dt_{1}\langle \beta |V(t_{1})|\alpha \rangle e^{-{\frac {i}{\hbar }}(E_{\alpha }-E_{\beta })(t_{1}-t_{0})}~,$ as detailed in the previous section——while the corresponding transition probability to a continuum is furnished by Fermi's golden rule.

As an aside, note that time-independent perturbation theory is also organized inside this time-dependent perturbation theory Dyson series. To see this, write the unitary evolution operator, obtained from the above Dyson series, as $U(t)=1-{\frac {i\lambda }{\hbar }}\int _{t_{0}}^{t}dt_{1}e^{{\frac {i}{\hbar }}H_{0}(t_{1}-t_{0})}V(t_{1})e^{-{\frac {i}{\hbar }}H_{0}(t_{1}-t_{0})}-{\frac {\lambda ^{2}}{\hbar ^{2}}}\int _{t_{0}}^{t}dt_{1}\int _{t_{0}}^{t_{1}}dt_{2}e^{{\frac {i}{\hbar }}H_{0}(t_{1}-t_{0})}V(t_{1})e^{-{\frac {i}{\hbar }}H_{0}(t_{1}-t_{0})}e^{{\frac {i}{\hbar }}H_{0}(t_{2}-t_{0})}V(t_{2})e^{-{\frac {i}{\hbar }}H_{0}(t_{2}-t_{0})}+\cdots$ and take the perturbation V to be time-independent.

Using the identity resolution $\sum _{n}|n\rangle \langle n|=1$ with $H_{0}|n\rangle =E_{n}|n\rangle$ for a pure discrete spectrum, write ${\begin{aligned}U(t)=1&-\left[{\frac {i\lambda }{\hbar }}\int _{t_{0}}^{t}dt_{1}\sum _{m}\sum _{n}\langle m|V|n\rangle e^{-{\frac {i}{\hbar }}(E_{n}-E_{m})(t_{1}-t_{0})}|m\rangle \langle n|\right]\\[5mu]&-\left[{\frac {\lambda ^{2}}{\hbar ^{2}}}\int _{t_{0}}^{t}dt_{1}\int _{t_{0}}^{t_{1}}dt_{2}\sum _{m}\sum _{n}\sum _{q}e^{-{\frac {i}{\hbar }}(E_{n}-E_{m})(t_{1}-t_{0})}\langle m|V|n\rangle \langle n|V|q\rangle e^{-{\frac {i}{\hbar }}(E_{q}-E_{n})(t_{2}-t_{0})}|m\rangle \langle q|\right]+\cdots \end{aligned}}$

It is evident that, at second order, one must sum on all the intermediate states. Assume $t_{0}=0$ and the asymptotic limit of larger times. This means that, at each contribution of the perturbation series, one has to add a multiplicative factor $e^{-\epsilon t}$ in the integrands for ε arbitrarily small. Thus the limit *t* → ∞ gives back the final state of the system by eliminating all oscillating terms, but keeping the secular ones. The integrals are thus computable, and, separating the diagonal terms from the others yields ${\begin{aligned}U(t)=1&-{\frac {i\lambda }{\hbar }}\sum _{n}\langle n|V|n\rangle t-{\frac {i\lambda ^{2}}{\hbar }}\sum _{m\neq n}{\frac {\langle n|V|m\rangle \langle m|V|n\rangle }{E_{n}-E_{m}}}t-{\frac {1}{2}}{\frac {\lambda ^{2}}{\hbar ^{2}}}\sum _{m,n}\langle n|V|m\rangle \langle m|V|n\rangle t^{2}+\cdots \\&+\lambda \sum _{m\neq n}{\frac {\langle m|V|n\rangle }{E_{n}-E_{m}}}|m\rangle \langle n|+\lambda ^{2}\sum _{m\neq n}\sum _{q\neq n}\sum _{n}{\frac {\langle m|V|n\rangle \langle n|V|q\rangle }{(E_{n}-E_{m})(E_{q}-E_{n})}}|m\rangle \langle q|+\cdots \end{aligned}}$ where the time secular series yields the eigenvalues of the perturbed problem specified above, recursively; whereas the remaining time-constant part yields the corrections to the stationary eigenfunctions also given above ( $|n(\lambda )\rangle =U(0;\lambda )|n\rangle )$ .)

The unitary evolution operator is applicable to arbitrary eigenstates of the unperturbed problem and, in this case, yields a secular series that holds at small times.


## Strong perturbation theory

In a similar way as for small perturbations, it is possible to develop a strong perturbation theory. Consider as usual the Schrödinger equation

$H(t)|\psi (t)\rangle =i\hbar {\frac {\partial |\psi (t)\rangle }{\partial t}}$

and we consider the question if a dual Dyson series exists that applies in the limit of a perturbation increasingly large. This question can be answered in an affirmative way and the series is the well-known adiabatic series. This approach is quite general and can be shown in the following way. Consider the perturbation problem

$[H_{0}+\lambda V(t)]|\psi (t)\rangle =i\hbar {\frac {\partial |\psi (t)\rangle }{\partial t}}$

being *λ*→ ∞. Our aim is to find a solution in the form

$|\psi \rangle =|\psi _{0}\rangle +{\frac {1}{\lambda }}|\psi _{1}\rangle +{\frac {1}{\lambda ^{2}}}|\psi _{2}\rangle +\ldots$

but a direct substitution into the above equation fails to produce useful results. This situation can be adjusted making a rescaling of the time variable as $\tau =\lambda t$ producing the following meaningful equations

${\begin{aligned}V(t)|\psi _{0}\rangle &=i\hbar {\frac {\partial |\psi _{0}\rangle }{\partial \tau }}\\[1ex]V(t)|\psi _{1}\rangle +H_{0}|\psi _{0}\rangle &=i\hbar {\frac {\partial |\psi _{1}\rangle }{\partial \tau }}\\[1ex]&\;\,\vdots \end{aligned}}$

that can be solved once we know the solution of the leading order equation. But we know that in this case we can use the adiabatic approximation. When $V(t)$ does not depend on time one gets the Wigner-Kirkwood series that is often used in statistical mechanics. Indeed, in this case we introduce the unitary transformation

$|\psi (t)\rangle =e^{-{\frac {i}{\hbar }}\lambda V(t-t_{0})}|\psi _{F}(t)\rangle$

that defines a **free picture** as we are trying to eliminate the interaction term. Now, in dual way with respect to the small perturbations, we have to solve the Schrödinger equation

$e^{{\frac {i}{\hbar }}\lambda V(t-t_{0})}H_{0}e^{-{\frac {i}{\hbar }}\lambda V(t-t_{0})}|\psi _{F}(t)\rangle =i\hbar {\frac {\partial |\psi _{F}(t)\rangle }{\partial t}}$

and we see that the expansion parameter λ appears only into the exponential and so, the corresponding Dyson series, a **dual Dyson series**, is meaningful at large λs and is

$|\psi _{F}(t)\rangle =\left[1-{\frac {i}{\hbar }}\int _{t_{0}}^{t}dt_{1}e^{{\frac {i}{\hbar }}\lambda V(t_{1}-t_{0})}H_{0}e^{-{\frac {i}{\hbar }}\lambda V(t_{1}-t_{0})}-{\frac {1}{\hbar ^{2}}}\int _{t_{0}}^{t}dt_{1}\int _{t_{0}}^{t_{1}}dt_{2}e^{{\frac {i}{\hbar }}\lambda V(t_{1}-t_{0})}H_{0}e^{-{\frac {i}{\hbar }}\lambda V(t_{1}-t_{0})}e^{{\frac {i}{\hbar }}\lambda V(t_{2}-t_{0})}H_{0}e^{-{\frac {i}{\hbar }}\lambda V(t_{2}-t_{0})}+\cdots \right]|\psi (t_{0})\rangle .$

After the rescaling in time $\tau =\lambda t$ we can see that this is indeed a series in $1/\lambda$ justifying in this way the name of **dual Dyson series**. The reason is that we have obtained this series simply interchanging *H*0 and V and we can go from one to another applying this exchange. This is called **duality principle** in perturbation theory. The choice $H_{0}=p^{2}/2m$ yields, as already said, a Wigner-Kirkwood series that is a gradient expansion. The Wigner-Kirkwood series is a semiclassical series with eigenvalues given exactly as for WKB approximation.


## Examples

### Example of first-order perturbation theory – ground-state energy of the quartic oscillator

Consider the quantum harmonic oscillator with the quartic potential perturbation and the Hamiltonian $H=-{\frac {\hbar ^{2}}{2m}}{\frac {\partial ^{2}}{\partial x^{2}}}+{\frac {m\omega ^{2}x^{2}}{2}}+\lambda x^{4}.$

The ground state of the harmonic oscillator is $\psi _{0}=\left({\frac {\alpha }{\pi }}\right)^{\frac {1}{4}}e^{-\alpha x^{2}/2}$ ( $\alpha =m\omega /\hbar$ ), and the energy of unperturbed ground state is $E_{0}^{(0)}={\tfrac {1}{2}}\hbar \omega$

Using the first-order correction formula, we get $E_{0}^{(1)}=\lambda \left({\frac {\alpha }{\pi }}\right)^{\frac {1}{2}}\int e^{-\alpha x^{2}/2}x^{4}e^{-\alpha x^{2}/2}dx=\lambda \left({\frac {\alpha }{\pi }}\right)^{\frac {1}{2}}{\frac {\partial ^{2}}{\partial \alpha ^{2}}}\int e^{-\alpha x^{2}}dx,$ or $E_{0}^{(1)}=\lambda \left({\frac {\alpha }{\pi }}\right)^{\frac {1}{2}}{\frac {\partial ^{2}}{\partial \alpha ^{2}}}\left({\frac {\pi }{\alpha }}\right)^{\frac {1}{2}}=\lambda {\frac {3}{4}}{\frac {1}{\alpha ^{2}}}={\frac {3}{4}}{\frac {\hbar ^{2}\lambda }{m^{2}\omega ^{2}}}.$

### Example of first- and second-order perturbation theory – quantum pendulum

Consider the quantum-mathematical pendulum with the Hamiltonian $H=-{\frac {\hbar ^{2}}{2ma^{2}}}{\frac {\partial ^{2}}{\partial \phi ^{2}}}-\lambda \cos \phi$ with the potential energy $-\lambda \cos \phi$ taken as the perturbation i.e. $V=-\cos \phi .$

The unperturbed normalized quantum wave functions are those of the rigid rotor and are given by $\psi _{n}(\phi )={\frac {e^{in\phi }}{\sqrt {2\pi }}},$ and the energies $E_{n}^{(0)}={\frac {\hbar ^{2}n^{2}}{2ma^{2}}}.$

The first-order energy correction to the rotor due to the potential energy is $E_{n}^{(1)}=-{\frac {1}{2\pi }}\int e^{-in\phi }\cos \phi e^{in\phi }=-{\frac {1}{2\pi }}\int \cos \phi =0.$

Using the formula for the second-order correction, one gets $E_{n}^{(2)}={\frac {ma^{2}}{2\pi ^{2}\hbar ^{2}}}\sum _{k}{\frac {\left|\int e^{-ik\phi }\cos \phi e^{in\phi }\,d\phi \right|^{2}}{n^{2}-k^{2}}},$ or $E_{n}^{(2)}={\frac {ma^{2}}{2\hbar ^{2}}}\sum _{k}{\frac {\left|\left(\delta _{n,1-k}+\delta _{n,-1-k}\right)\right|^{2}}{n^{2}-k^{2}}},$ or $E_{n}^{(2)}={\frac {ma^{2}}{2\hbar ^{2}}}\left({\frac {1}{2n-1}}+{\frac {1}{-2n-1}}\right)={\frac {ma^{2}}{\hbar ^{2}}}{\frac {1}{4n^{2}-1}}.$

### Potential energy as a perturbation

When the unperturbed state is a free motion of a particle with kinetic energy E , the solution of the Schrödinger equation $\nabla ^{2}\psi ^{(0)}+k^{2}\psi ^{(0)}=0$ corresponds to plane waves with wavenumber ${\textstyle k={\sqrt {2mE/\hbar ^{2}}}}$ . If there is a weak potential energy $U(x,y,z)$ present in the space, in the first approximation, the perturbed state is described by the equation $\nabla ^{2}\psi ^{(1)}+k^{2}\psi ^{(1)}={\frac {2mU}{\hbar ^{2}}}\psi ^{(0)},$ whose particular integral is $\psi ^{(1)}(x,y,z)=-{\frac {m}{2\pi \hbar ^{2}}}\int \psi ^{(0)}U(x',y',z'){\frac {e^{ikr}}{r}}\,dx'dy'dz',$ where $r^{2}=(x-x')^{2}+(y-y')^{2}+(z-z')^{2}$ . In the two-dimensional case, the solution is $\psi ^{(1)}(x,y)=-{\frac {im}{2\hbar ^{2}}}\int \psi ^{(0)}U(x',y')H_{0}^{(1)}(kr)\,dx'dy',$ where $r^{2}=(x-x')^{2}+(y-y')^{2}$ and $H_{0}^{(1)}$ is the Hankel function of the first kind. In the one-dimensional case, the solution is $\psi ^{(1)}(x)=-{\frac {im}{\hbar ^{2}}}\int \psi ^{(0)}U(x'){\frac {e^{ikr}}{k}}\,dx',$ where $r=|x-x'|$ .


## Applications

- Rabi cycle
- Fermi's golden rule
- Muon spin spectroscopy
- Perturbed angular correlation
