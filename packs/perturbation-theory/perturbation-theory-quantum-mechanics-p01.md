---
title: "Perturbation theory (quantum mechanics) (part 1/2)"
source: https://en.wikipedia.org/wiki/Perturbation_theory_(quantum_mechanics)
domain: perturbation-theory
license: CC-BY-SA-4.0
tags: perturbation theory, method of averaging, multiple-scale analysis, adiabatic theorem
fetched: 2026-07-02
part: 1/2
---

# Perturbation theory (quantum mechanics)

In quantum mechanics, **perturbation theory** is a set of approximation schemes directly related to mathematical perturbation for describing a complicated quantum system in terms of a simpler, known system. The idea is to start with a simple system for which a mathematical solution is known (e.g. the time-independent Schrödinger equation: ${\hat {H}}|\Psi \rangle =E|\Psi \rangle$ ) and add an additional "perturbing" Hamiltonian ( $H'$ ) representing a weak disturbance to the known system to the original Hamiltonian ( $H_{0}$ ) of the known system (i.e. ${\hat {H}}=H_{0}+H'$ ). If the disturbance is small, the new energy levels and eigenstates of the perturbed system can be expressed as "corrections" to the known energy levels and eigenstates of the simpler system. These corrections can be made at progressively smaller orders of magnitude until an n-th order that is so small a correction that it is negligible to the accuracy of the approximation.


## Approximate Hamiltonians

Perturbation theory is an important tool for describing quantum systems without exact solutions. Systems with known exact solutions, such as the hydrogen atom, the quantum harmonic oscillator, and the particle in a box, are idealized and may not adequately describe related systems. Perturbation theory uses known solutions to generate solutions for more complicated systems. The procedure uses approximations to the system Hamiltonian.


## Applying perturbation theory

Perturbation theory is applicable if the problem at hand cannot be solved exactly, but can be formulated by adding a "small" term to the mathematical description of the exactly solvable problem.

For example, by adding a perturbative electric potential to the quantum mechanical model of the hydrogen atom, tiny shifts in the spectral lines of hydrogen caused by the presence of an electric field (the Stark effect) can be calculated. This is only approximate because the sum of a Coulomb potential with a linear potential is unstable (has no true bound states) although the tunneling time (decay rate) is very long. This instability shows up as a broadening of the energy spectrum lines, which perturbation theory fails to reproduce entirely.

The expressions produced by perturbation theory are not exact, but they can lead to accurate results as long as the expansion parameter, say α, is very small. Typically, the results are expressed in terms of finite power series in α that seem to converge to the exact values when summed to higher order. After a certain order *n* ~ 1/*α* however, the results become increasingly worse since the series are usually divergent (being asymptotic series). There exist ways to convert them into convergent series, which can be evaluated for large-expansion parameters, most efficiently by the variational method. In practice, convergent perturbation expansions often converge slowly while divergent perturbation expansions sometimes give good results, c.f. the exact solution, at lower order.

In the theory of quantum electrodynamics (QED), in which the electron–photon interaction is treated perturbatively, the calculation of the electron's magnetic moment has been found to agree with experiment to eleven decimal places. In QED and other quantum field theories, special calculation techniques known as Feynman diagrams are used to systematically sum the power series terms.

### Limitations

#### Large perturbations

Some systems cannot be describe by a small perturbation imposed on some simple system. Perturbation theory requires small perturbations. In quantum chromodynamics, for instance, the interaction of quarks with the gluon field cannot be treated perturbatively at low energies because the coupling constant (the expansion parameter) becomes too large, violating the requirement that corrections must be small.

#### Non-adiabatic states

Perturbation theory also fails to describe states that are not generated adiabatically from the "free model", including bound states and various collective phenomena such as solitons. A system of free (i.e. non-interacting) particles, to which an attractive interaction is introduced, may create an entirely new set of eigenstates corresponding to groups of particles bound to one another. An example of this phenomenon may be found in conventional superconductivity, in which the phonon-mediated attraction between conduction electrons leads to the formation of correlated electron pairs known as Cooper pairs. Perturbation theory fails because there is no analogue of a bound particle in the unperturbed model and the energy of a soliton typically goes as the *inverse* of the expansion parameter. Other approximation schemes, such as the variational method and the WKB approximation may apply to these cases.

#### Difficult computations

The problem of non-perturbative systems has been somewhat alleviated by the advent of modern computers. It has become practical to obtain numerical non-perturbative solutions for certain problems, using methods such as density functional theory. These advances have been of particular benefit to the field of quantum chemistry. Computers have also been used to carry out perturbation theory calculations to extraordinarily high levels of precision, which has proven important in particle physics for generating theoretical results that can be compared with experiment.


## Time-independent perturbation theory

Time-independent perturbation theory is one of two categories of perturbation theory, the other being time-dependent perturbation (see next section). In time-independent perturbation theory, the perturbation Hamiltonian is static (i.e., possesses no time dependence). Time-independent perturbation theory was presented by Erwin Schrödinger in a 1926 paper, shortly after he produced his theories in wave mechanics. In this paper Schrödinger referred to earlier work of Lord Rayleigh, who investigated harmonic vibrations of a string perturbed by small inhomogeneities. This is why this perturbation theory is often referred to as **Rayleigh–Schrödinger perturbation theory**. Time-independent perturbation theory can itself be separated into non-degenerate and degenerate perturbation theory.

### Non-degenerate perturbation theory

#### First order corrections

The process begins with an unperturbed Hamiltonian *H*0, which is assumed to have no time dependence. It has known energy levels and eigenstates, arising from the time-independent Schrödinger equation:

$H_{0}\left|n^{(0)}\right\rangle =E_{n}^{(0)}\left|n^{(0)}\right\rangle ,\qquad n=1,2,3,\cdots$

For simplicity, it is assumed that the energies are discrete. The (0) superscripts denote that these quantities are associated with the unperturbed system. Note the use of bra–ket notation.

A perturbation is then introduced to the Hamiltonian. Let V be a Hamiltonian representing a weak physical disturbance, such as a potential energy produced by an external field. Thus, V is formally a Hermitian operator. Let λ be a dimensionless parameter that can take on values ranging continuously from 0 (no perturbation) to 1 (the full perturbation). The perturbed Hamiltonian is:

$H=H_{0}+\lambda V$

The energy levels and eigenstates of the perturbed Hamiltonian are again given by the time-independent Schrödinger equation, $\left(H_{0}+\lambda V\right)|n\rangle =E_{n}|n\rangle .$

The objective is to express En and $|n\rangle$ in terms of the energy levels and eigenstates of the old Hamiltonian. If the perturbation is sufficiently weak, they can be written as a (Maclaurin) power series in λ, ${\begin{aligned}E_{n}&=E_{n}^{(0)}+\lambda E_{n}^{(1)}+\lambda ^{2}E_{n}^{(2)}+\cdots \\[1ex]|n\rangle &=\left|n^{(0)}\right\rangle +\lambda \left|n^{(1)}\right\rangle +\lambda ^{2}\left|n^{(2)}\right\rangle +\cdots \end{aligned}}$ where ${\begin{aligned}E_{n}^{(k)}&={\frac {1}{k!}}{\frac {d^{k}E_{n}}{d\lambda ^{k}}}{\bigg |}_{\lambda =0}\\[1ex]\left|n^{(k)}\right\rangle &=\left.{\frac {1}{k!}}{\frac {d^{k}|n\rangle }{d\lambda ^{k}}}\right|_{\lambda =0.}\end{aligned}}$

When *k* = 0, these reduce to the unperturbed values, which are the first term in each series. Since the perturbation is weak, the energy levels and eigenstates should not deviate too much from their unperturbed values, and the terms should rapidly become smaller as the order is increased.

Substituting the power series expansion into the Schrödinger equation produces:

$\left(H_{0}+\lambda V\right)\left(\left|n^{(0)}\right\rangle +\lambda \left|n^{(1)}\right\rangle +\cdots \right)=\left(E_{n}^{(0)}+\lambda E_{n}^{(1)}+\cdots \right)\left(\left|n^{(0)}\right\rangle +\lambda \left|n^{(1)}\right\rangle +\cdots \right).$

Expanding this equation and comparing coefficients of each power of λ results in an infinite series of simultaneous equations. The zeroth-order equation is simply the Schrödinger equation for the unperturbed system, $H_{0}\left|n^{(0)}\right\rangle =E_{n}^{(0)}\left|n^{(0)}\right\rangle .$

The first-order equation is $H_{0}\left|n^{(1)}\right\rangle +V\left|n^{(0)}\right\rangle =E_{n}^{(0)}\left|n^{(1)}\right\rangle +E_{n}^{(1)}\left|n^{(0)}\right\rangle .$

Operating through by $\langle n^{(0)}|$ , the first term on the left-hand side cancels the first term on the right-hand side. (Recall, the unperturbed Hamiltonian is Hermitian). This leads to the first-order energy shift, $E_{n}^{(1)}=\left\langle n^{(0)}\right|V\left|n^{(0)}\right\rangle .$ This is simply the expectation value of the perturbation Hamiltonian while the system is in the unperturbed eigenstate.

This result can be interpreted in the following way: supposing that the perturbation is applied, but the system is kept in the quantum state $|n^{(0)}\rangle$ , which is a valid quantum state though no longer an energy eigenstate. The perturbation causes the average energy of this state to increase by $\langle n^{(0)}|V|n^{(0)}\rangle$ . However, the true energy shift is slightly different, because the perturbed eigenstate is not exactly the same as $|n^{(0)}\rangle$ . These further shifts are given by the second and higher order corrections to the energy.

Before corrections to the energy eigenstate are computed, the issue of normalization must be addressed. Supposing that $\left\langle n^{(0)}\right|\left.n^{(0)}\right\rangle =1,$ but perturbation theory also assumes that $\langle n|n\rangle =1$ .

Then at first order in λ, the following must be true: $\left(\left\langle n^{(0)}\right|+\lambda \left\langle n^{(1)}\right|\right)\left(\left|n^{(0)}\right\rangle +\lambda \left|n^{(1)}\right\rangle \right)=1$ $\left\langle n^{(0)}\right|\left.n^{(0)}\right\rangle +\lambda \left\langle n^{(0)}\right|\left.n^{(1)}\right\rangle +\lambda \left\langle n^{(1)}\right|\left.n^{(0)}\right\rangle +{\cancel {\lambda ^{2}\left\langle n^{(1)}\right|\left.n^{(1)}\right\rangle }}=1$ $\left\langle n^{(0)}\right|\left.n^{(1)}\right\rangle +\left\langle n^{(1)}\right|\left.n^{(0)}\right\rangle =0.$

The 𝜆2 term is dropped in first-order expansions.

Since the overall phase is not determined in quantum mechanics, without loss of generality, in time-independent theory it can be assumed that $\langle n^{(0)}|n^{(1)}\rangle$ is purely real. Therefore, $\left\langle n^{(0)}\right|\left.n^{(1)}\right\rangle =\left\langle n^{(1)}\right|\left.n^{(0)}\right\rangle =-\left\langle n^{(1)}\right|\left.n^{(0)}\right\rangle ,$ leading to $\left\langle n^{(0)}\right|\left.n^{(1)}\right\rangle =0.$

To obtain the first-order correction to the energy eigenstate, the expression for the first-order energy correction is inserted back into the result shown above, equating the first-order coefficients of λ.

The first-order correction to the energy eigenstate can also be obtained through the following considerations. By using the resolution of the identity: ${\begin{aligned}V\left|n^{(0)}\right\rangle &=\left(\sum _{k}\left|k^{(0)}\right\rangle \left\langle k^{(0)}\right|\right)V\left|n^{(0)}\right\rangle \\&=\left(\sum _{k\neq n}\left|k^{(0)}\right\rangle \left\langle k^{(0)}\right|\right)V\left|n^{(0)}\right\rangle +\left(\left|n^{(0)}\right\rangle \left\langle n^{(0)}\right|\right)V\left|n^{(0)}\right\rangle \\&=\sum _{k\neq n}\left|k^{(0)}\right\rangle \left\langle k^{(0)}\right|V\left|n^{(0)}\right\rangle +E_{n}^{(1)}\left|n^{(0)}\right\rangle ,\end{aligned}}$ where the $|k^{(0)}\rangle$ are in the orthogonal complement of $|n^{(0)}\rangle$ , i.e., the other eigenvectors.

The first-order equation may thus be expressed as $\left(E_{n}^{(0)}-H_{0}\right)\left|n^{(1)}\right\rangle =\sum _{k\neq n}\left|k^{(0)}\right\rangle \left\langle k^{(0)}\right|V\left|n^{(0)}\right\rangle .$

Suppose that the zeroth-order energy level is not degenerate, i.e. that there is no eigenstate of *H*0 in the orthogonal complement of $|n^{(0)}\rangle$ with the energy $E_{n}^{(0)}$ . After renaming the summation dummy index above as $k'$ , any $k\neq n$ can be chosen and multiplying the first-order equation through by $\langle k^{(0)}|$ gives $\left(E_{n}^{(0)}-E_{k}^{(0)}\right)\left\langle k^{(0)}\right.\left|n^{(1)}\right\rangle =\left\langle k^{(0)}\right|V\left|n^{(0)}\right\rangle .$

The above $\langle k^{(0)}|n^{(1)}\rangle$ is, by definition, the component of the first-order correction $|n^{(1)}\rangle$ along $|k^{(0)}\rangle$ . Thus, in the *H*0 basis, $|n^{(1)}\rangle$ can be expressed as: $\left|n^{(1)}\right\rangle =\sum _{k\neq n}{\frac {\left\langle k^{(0)}\right|V\left|n^{(0)}\right\rangle }{E_{n}^{(0)}-E_{k}^{(0)}}}\left|k^{(0)}\right\rangle .$

The first-order change in the n-th energy eigenstate has a contribution from each of the other energy eigenstates *k* ≠ *n*. Each term is proportional to the matrix element $\langle k^{(0)}|V|n^{(0)}\rangle$ , which is a measure of how much the perturbation mixes eigenstate n with eigenstate k; it is also inversely proportional to the energy difference between eigenstates k and n, which means that the perturbation deforms the eigenstate to a greater extent if there are more eigenstates at nearby energies. The expression is singular if any of these states have the same energy as state n, which is why it was assumed that there is no degeneracy. The above formula for the perturbed eigenstates also implies that the perturbation theory can be legitimately used only when the absolute magnitude of the matrix elements of the perturbation is small compared with the corresponding differences in the unperturbed energy levels, i.e., $|\langle k^{(0)}|V|n^{(0)}\rangle |\ll |E_{n}^{(0)}-E_{k}^{(0)}|.$

#### Second-order and higher-order corrections

Higher-order deviations are calculated by a similar procedure, though the calculations become quite tedious within this formulation. Normalization convention, of the whole state vectors of the perturbed Schrodinger equation being orthonormal, gives

$2\operatorname {Re} (\left\langle n^{(0)}\right|\left.n^{(2)}\right\rangle )+\left\langle n^{(1)}\right|\left.n^{(1)}\right\rangle =0.$

We will bring a phase to the whole state vector of the perturbed Schrodinger equation which will lead to the first term having only a real part. Up to second order, the expressions for the energies and (normalized) eigenstates are:

$E_{n}^{(2)}(\lambda )=E_{n}^{(0)}+\lambda \left\langle n^{(0)}\right|V\left|n^{(0)}\right\rangle +\lambda ^{2}\sum _{k\neq n}{\frac {\left|\left\langle k^{(0)}\right|V\left|n^{(0)}\right\rangle \right|^{2}}{E_{n}^{(0)}-E_{k}^{(0)}}}+O(\lambda ^{3})$

${\begin{aligned}|n^{(2)}(\lambda )\rangle =\left|n^{(0)}\right\rangle &+\lambda \sum _{k\neq n}\left|k^{(0)}\right\rangle {\frac {\left\langle k^{(0)}\right|V\left|n^{(0)}\right\rangle }{E_{n}^{(0)}-E_{k}^{(0)}}}+\lambda ^{2}\sum _{k\neq n}\sum _{\ell \neq n}\left|k^{(0)}\right\rangle {\frac {\left\langle k^{(0)}\right|V\left|\ell ^{(0)}\right\rangle \left\langle \ell ^{(0)}\right|V\left|n^{(0)}\right\rangle }{\left(E_{n}^{(0)}-E_{k}^{(0)}\right)\left(E_{n}^{(0)}-E_{\ell }^{(0)}\right)}}\\[1ex]&-\lambda ^{2}\sum _{k\neq n}\left|k^{(0)}\right\rangle {\frac {\left\langle k^{(0)}\right|V\left|n^{(0)}\right\rangle \left\langle n^{(0)}\right|V\left|n^{(0)}\right\rangle }{\left(E_{n}^{(0)}-E_{k}^{(0)}\right)^{2}}}-{\frac {1}{2}}\lambda ^{2}\left|n^{(0)}\right\rangle \sum _{k\neq n}{\frac {|\left\langle k^{(0)}\right|V\left|n^{(0)}\right\rangle |^{2}}{\left(E_{n}^{(0)}-E_{k}^{(0)}\right)^{2}}}+O(\lambda ^{3}).\end{aligned}}$ If an intermediate normalization is taken (in other words, if it is required that $\langle n^{(0)}|n(\lambda )\rangle =1$ ), then we obtain a nearly identical expression for the second-order correction to the correction given immediately above. To be precise, for an intermediate normalization, the last term would be omitted.

Extending the process further, the third-order energy correction can be shown to be

$E_{n}^{(3)}=\sum _{k\neq n}\sum _{m\neq n}{\frac {\langle n^{(0)}|V|m^{(0)}\rangle \langle m^{(0)}|V|k^{(0)}\rangle \langle k^{(0)}|V|n^{(0)}\rangle }{\left(E_{n}^{(0)}-E_{m}^{(0)}\right)\left(E_{n}^{(0)}-E_{k}^{(0)}\right)}}-\langle n^{(0)}|V|n^{(0)}\rangle \sum _{m\neq n}{\frac {|\langle n^{(0)}|V|m^{(0)}\rangle |^{2}}{\left(E_{n}^{(0)}-E_{m}^{(0)}\right)^{2}}}.$

Corrections to fifth order (energies) and fourth order (states) in compact notation

If we introduce the notation,

$V_{nm}\equiv \langle n^{(0)}|V|m^{(0)}\rangle ,$ $E_{nm}\equiv E_{n}^{(0)}-E_{m}^{(0)},$

then the energy corrections to fifth order can be written

${\begin{aligned}E_{n}^{(1)}&=V_{nn}\\E_{n}^{(2)}&={\frac {|V_{nk_{2}}|^{2}}{E_{nk_{2}}}}\\E_{n}^{(3)}&={\frac {V_{nk_{3}}V_{k_{3}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{3}}}}-V_{nn}{\frac {|V_{nk_{3}}|^{2}}{E_{nk_{3}}^{2}}}\\E_{n}^{(4)}&={\frac {V_{nk_{4}}V_{k_{4}k_{3}}V_{k_{3}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{3}}E_{nk_{4}}}}-{\frac {|V_{nk_{4}}|^{2}}{E_{nk_{4}}^{2}}}{\frac {|V_{nk_{2}}|^{2}}{E_{nk_{2}}}}-V_{nn}{\frac {V_{nk_{4}}V_{k_{4}k_{3}}V_{k_{3}n}}{E_{nk_{3}}^{2}E_{nk_{4}}}}-V_{nn}{\frac {V_{nk_{4}}V_{k_{4}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{4}}^{2}}}+V_{nn}^{2}{\frac {|V_{nk_{4}}|^{2}}{E_{nk_{4}}^{3}}}\\&={\frac {V_{nk_{4}}V_{k_{4}k_{3}}V_{k_{3}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{3}}E_{nk_{4}}}}-E_{n}^{(2)}{\frac {|V_{nk_{4}}|^{2}}{E_{nk_{4}}^{2}}}-2V_{nn}{\frac {V_{nk_{4}}V_{k_{4}k_{3}}V_{k_{3}n}}{E_{nk_{3}}^{2}E_{nk_{4}}}}+V_{nn}^{2}{\frac {|V_{nk_{4}}|^{2}}{E_{nk_{4}}^{3}}}\\E_{n}^{(5)}&={\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}k_{3}}V_{k_{3}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{3}}E_{nk_{4}}E_{nk_{5}}}}-{\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}n}}{E_{nk_{4}}^{2}E_{nk_{5}}}}{\frac {|V_{nk_{2}}|^{2}}{E_{nk_{2}}}}-{\frac {V_{nk_{5}}V_{k_{5}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{5}}^{2}}}{\frac {|V_{nk_{2}}|^{2}}{E_{nk_{2}}}}-{\frac {|V_{nk_{5}}|^{2}}{E_{nk_{5}}^{2}}}{\frac {V_{nk_{3}}V_{k_{3}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{3}}}}\\&\quad -V_{nn}{\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}k_{3}}V_{k_{3}n}}{E_{nk_{3}}^{2}E_{nk_{4}}E_{nk_{5}}}}-V_{nn}{\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{4}}^{2}E_{nk_{5}}}}-V_{nn}{\frac {V_{nk_{5}}V_{k_{5}k_{3}}V_{k_{3}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{3}}E_{nk_{5}}^{2}}}+V_{nn}{\frac {|V_{nk_{5}}|^{2}}{E_{nk_{5}}^{2}}}{\frac {|V_{nk_{3}}|^{2}}{E_{nk_{3}}^{2}}}+2V_{nn}{\frac {|V_{nk_{5}}|^{2}}{E_{nk_{5}}^{3}}}{\frac {|V_{nk_{2}}|^{2}}{E_{nk_{2}}}}\\&\quad +V_{nn}^{2}{\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}n}}{E_{nk_{4}}^{3}E_{nk_{5}}}}+V_{nn}^{2}{\frac {V_{nk_{5}}V_{k_{5}k_{3}}V_{k_{3}n}}{E_{nk_{3}}^{2}E_{nk_{5}}^{2}}}+V_{nn}^{2}{\frac {V_{nk_{5}}V_{k_{5}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{5}}^{3}}}-V_{nn}^{3}{\frac {|V_{nk_{5}}|^{2}}{E_{nk_{5}}^{4}}}\\&={\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}k_{3}}V_{k_{3}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{3}}E_{nk_{4}}E_{nk_{5}}}}-2E_{n}^{(2)}{\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}n}}{E_{nk_{4}}^{2}E_{nk_{5}}}}-{\frac {|V_{nk_{5}}|^{2}}{E_{nk_{5}}^{2}}}{\frac {V_{nk_{3}}V_{k_{3}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{3}}}}\\&\quad +V_{nn}\left(-2{\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}k_{3}}V_{k_{3}n}}{E_{nk_{3}}^{2}E_{nk_{4}}E_{nk_{5}}}}-{\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}k_{2}}V_{k_{2}n}}{E_{nk_{2}}E_{nk_{4}}^{2}E_{nk_{5}}}}+{\frac {|V_{nk_{5}}|^{2}}{E_{nk_{5}}^{2}}}{\frac {|V_{nk_{3}}|^{2}}{E_{nk_{3}}^{2}}}+2E_{n}^{(2)}{\frac {|V_{nk_{5}}|^{2}}{E_{nk_{5}}^{3}}}\right)\\&\quad +V_{nn}^{2}\left(2{\frac {V_{nk_{5}}V_{k_{5}k_{4}}V_{k_{4}n}}{E_{nk_{4}}^{3}E_{nk_{5}}}}+{\frac {V_{nk_{5}}V_{k_{5}k_{3}}V_{k_{3}n}}{E_{nk_{3}}^{2}E_{nk_{5}}^{2}}}\right)-V_{nn}^{3}{\frac {|V_{nk_{5}}|^{2}}{E_{nk_{5}}^{4}}}\end{aligned}}$ and the states to fourth order can be written ${\begin{aligned}|n^{(1)}\rangle &={\frac {V_{k_{1}n}}{E_{nk_{1}}}}|k_{1}^{(0)}\rangle \\|n^{(2)}\rangle &=\left({\frac {V_{k_{1}k_{2}}V_{k_{2}n}}{E_{nk_{1}}E_{nk_{2}}}}-{\frac {V_{nn}V_{k_{1}n}}{E_{nk_{1}}^{2}}}\right)|k_{1}^{(0)}\rangle -{\frac {1}{2}}{\frac {V_{nk_{1}}V_{k_{1}n}}{E_{k_{1}n}^{2}}}|n^{(0)}\rangle \\|n^{(3)}\rangle &={\Bigg [}-{\frac {V_{k_{1}k_{2}}V_{k_{2}k_{3}}V_{k_{3}n}}{E_{k_{1}n}E_{nk_{2}}E_{nk_{3}}}}+{\frac {V_{nn}V_{k_{1}k_{2}}V_{k_{2}n}}{E_{k_{1}n}E_{nk_{2}}}}\left({\frac {1}{E_{nk_{1}}}}+{\frac {1}{E_{nk_{2}}}}\right)-{\frac {|V_{nn}|^{2}V_{k_{1}n}}{E_{k_{1}n}^{3}}}+{\frac {|V_{nk_{2}}|^{2}V_{k_{1}n}}{E_{k_{1}n}E_{nk_{2}}}}\left({\frac {1}{E_{nk_{1}}}}+{\frac {1}{2E_{nk_{2}}}}\right){\Bigg ]}|k_{1}^{(0)}\rangle \\&\quad +{\Bigg [}-{\frac {V_{nk_{2}}V_{k_{2}k_{1}}V_{k_{1}n}+V_{k_{2}n}V_{k_{1}k_{2}}V_{nk_{1}}}{2E_{nk_{2}}^{2}E_{nk_{1}}}}+{\frac {|V_{nk_{1}}|^{2}V_{nn}}{E_{nk_{1}}^{3}}}{\Bigg ]}|n^{(0)}\rangle \\|n^{(4)}\rangle &={\Bigg [}{\frac {V_{k_{1}k_{2}}V_{k_{2}k_{3}}V_{k_{3}k_{4}}V_{k_{4}k_{2}}+V_{k_{3}k_{2}}V_{k_{1}k_{2}}V_{k_{4}k_{3}}V_{k_{2}k_{4}}}{2E_{k_{1}n}E_{k_{2}k_{3}}^{2}E_{k_{2}k_{4}}}}-{\frac {V_{k_{2}k_{3}}V_{k_{3}k_{4}}V_{k_{4}n}V_{k_{1}k_{2}}}{E_{k_{1}n}E_{k_{2}n}E_{nk_{3}}E_{nk_{4}}}}+{\frac {V_{k_{1}k_{2}}}{E_{k_{1}n}}}\left({\frac {|V_{k_{2}k_{3}}|^{2}V_{k_{2}k_{2}}}{E_{k_{2}k_{3}}^{3}}}-{\frac {|V_{nk_{3}}|^{2}V_{k_{2}n}}{E_{k_{3}n}^{2}E_{k_{2}n}}}\right)\\&\quad +{\frac {V_{nn}V_{k_{1}k_{2}}V_{k_{3}n}V_{k_{2}k_{3}}}{E_{k_{1}n}E_{nk_{3}}E_{k_{2}n}}}\left({\frac {1}{E_{nk_{3}}}}+{\frac {1}{E_{k_{2}n}}}+{\frac {1}{E_{k_{1}n}}}\right)+{\frac {|V_{k_{2}n}|^{2}V_{k_{1}k_{3}}}{E_{nk_{2}}E_{k_{1}n}}}\left({\frac {V_{k_{3}n}}{E_{nk_{1}}E_{nk_{3}}}}-{\frac {V_{k_{3}k_{1}}}{E_{k_{3}k_{1}}^{2}}}\right)-{\frac {V_{nn}\left(V_{k_{3}k_{2}}V_{k_{1}k_{3}}V_{k_{2}k_{1}}+V_{k_{3}k_{1}}V_{k_{2}k_{3}}V_{k_{1}k_{2}}\right)}{2E_{k_{1}n}E_{k_{1}k_{3}}^{2}E_{k_{1}k_{2}}}}\\&\quad +{\frac {|V_{nn}|^{2}}{E_{k_{1}n}}}\left({\frac {V_{k_{1}n}V_{nn}}{E_{k_{1}n}^{3}}}+{\frac {V_{k_{1}k_{2}}V_{k_{2}n}}{E_{k_{2}n}^{3}}}\right)-{\frac {|V_{k_{1}k_{2}}|^{2}V_{nn}V_{k_{1}n}}{E_{k_{1}n}E_{k_{1}k_{2}}^{3}}}{\Bigg ]}|k_{1}^{(0)}\rangle +{\frac {1}{2}}\left[{\frac {V_{nk_{1}}V_{k_{1}k_{2}}}{E_{nk_{1}}E_{k_{2}n}^{2}}}\left({\frac {V_{k_{2}n}V_{nn}}{E_{k_{2}n}}}-{\frac {V_{k_{2}k_{3}}V_{k_{3}n}}{E_{nk_{3}}}}\right)\right.\\&\quad \left.-{\frac {V_{k_{1}n}V_{k_{2}k_{1}}}{E_{k_{1}n}^{2}E_{nk_{2}}}}\left({\frac {V_{k_{3}k_{2}}V_{nk_{3}}}{E_{nk_{3}}}}+{\frac {V_{nn}V_{nk_{2}}}{E_{nk_{2}}}}\right)+{\frac {|V_{nk_{1}}|^{2}}{E_{k_{1}n}^{2}}}\left({\frac {3|V_{nk_{2}}|^{2}}{4E_{k_{2}n}^{2}}}-{\frac {2|V_{nn}|^{2}}{E_{k_{1}n}^{2}}}\right)-{\frac {V_{k_{2}k_{3}}V_{k_{3}k_{1}}|V_{nk_{1}}|^{2}}{E_{nk_{3}}^{2}E_{nk_{1}}E_{nk_{2}}}}\right]|n^{(0)}\rangle \end{aligned}}$

All terms involved kj should be summed over kj such that the denominator does not vanish.

It is possible to relate the *k*-th order correction to the energy *En* to the *k*-point connected correlation function of the perturbation *V* in the state $|n^{(0)}\rangle$ . For $k=2$ , one has to consider the inverse Laplace transform $\rho _{n,2}(s)$ of the two-point correlator: $\langle n^{(0)}|V(\tau )V(0)|n^{(0)}\rangle -\langle n^{(0)}|V|n^{(0)}\rangle ^{2}=\mathrel {\mathop {:} } \int _{\mathbb {R} }\!ds\;\rho _{n,2}(s)\,e^{-(s-E_{n}^{(0)})\tau }$ where $V(\tau )=e^{H_{0}\tau }Ve^{-H_{0}\tau }$ is the perturbing operator *V* in the interaction picture, evolving in Euclidean time. Then $E_{n}^{(2)}=-\int _{\mathbb {R} }\!{\frac {ds}{s-E_{n}^{(0)}}}\,\rho _{n,2}(s).$

Similar formulas exist to all orders in perturbation theory, allowing one to express $E_{n}^{(k)}$ in terms of the inverse Laplace transform $\rho _{n,k}$ of the connected correlation function $\langle n^{(0)}|V(\tau _{1}+\ldots +\tau _{k-1})\dotsm V(\tau _{1}+\tau _{2})V(\tau _{1})V(0)|n^{(0)}\rangle _{\text{conn}}=\langle n^{(0)}|V(\tau _{1}+\ldots +\tau _{k-1})\dotsm V(\tau _{1}+\tau _{2})V(\tau _{1})V(0)|n^{(0)}\rangle -{\text{subtractions}}.$

To be precise, if we write $\langle n^{(0)}|V(\tau _{1}+\ldots +\tau _{k-1})\dotsm V(\tau _{1}+\tau _{2})V(\tau _{1})V(0)|n^{(0)}\rangle _{\text{conn}}=\int _{\mathbb {R} }\,\prod _{i=1}^{k-1}ds_{i}\,e^{-(s_{i}-E_{n}^{(0)})\tau _{i}}\,\rho _{n,k}(s_{1},\ldots ,s_{k-1})\,$ then the *k*-th order energy shift is given by

$E_{n}^{(k)}=(-1)^{k-1}\int _{\mathbb {R} }\,\prod _{i=1}^{k-1}{\frac {ds_{i}}{s_{i}-E_{n}^{(0)}}}\,\rho _{n,k}(s_{1},\ldots ,s_{k-1}).$

### Degenerate perturbation theory

Suppose that two or more energy eigenstates of the unperturbed Hamiltonian are degenerate. The first-order energy shift is not well defined, since there is no unique way to choose a basis of eigenstates for the unperturbed system. The various eigenstates for a given energy will perturb with different energies, or may well possess no continuous family of perturbations at all.

This is manifested in the calculation of the perturbed eigenstate via the fact that the operator $E_{n}^{(0)}-H_{0}$ does not have a well-defined inverse.

Let D denote the subspace spanned by these degenerate eigenstates. No matter how small the perturbation is, in the degenerate subspace D the energy differences between the eigenstates of *H* are non-zero, so complete mixing of at least some of these states is assured. Typically, the eigenvalues will split, and the eigenspaces will become simple (one-dimensional), or at least of smaller dimension than *D*.

The successful perturbations will not be "small" relative to a poorly chosen basis of *D*. Instead, we consider the perturbation "small" if the new eigenstate is close to the subspace D. The new Hamiltonian must be diagonalized in D, or a slight variation of *D*, so to speak. These perturbed eigenstates in D are now the basis for the perturbation expansion, $|n\rangle =\sum _{k\in D}\alpha _{nk}|k^{(0)}\rangle +\lambda |n^{(1)}\rangle .$

For the first-order perturbation, we need solve the perturbed Hamiltonian restricted to the degenerate subspace D, $V|k^{(0)}\rangle =\epsilon _{k}|k^{(0)}\rangle +{\text{small}}\qquad \forall |k^{(0)}\rangle \in D,$ simultaneously for all the degenerate eigenstates, where $\epsilon _{k}$ are first-order corrections to the degenerate energy levels, and "small" is a vector of $O(\lambda )$ orthogonal to *D*. This amounts to diagonalizing the matrix $\langle k^{(0)}|V|l^{(0)}\rangle =V_{kl}\qquad \forall \;|k^{(0)}\rangle ,|l^{(0)}\rangle \in D.$

This procedure is approximate, since we neglected states outside the D subspace ("small"). The splitting of degenerate energies $\epsilon _{k}$ is generally observed. Although the splitting may be small, $O(\lambda )$ , compared to the range of energies found in the system, it is crucial in understanding certain details, such as spectral lines in Electron Spin Resonance experiments.

Higher-order corrections due to other eigenstates outside D can be found in the same way as for the non-degenerate case, $\left(E_{n}^{(0)}-H_{0}\right)|n^{(1)}\rangle =\sum _{k\not \in D}\left(\langle k^{(0)}|V|n^{(0)}\rangle \right)|k^{(0)}\rangle .$

The operator on the left-hand side is not singular when applied to eigenstates outside D, so we can write $|n^{(1)}\rangle =\sum _{k\not \in D}{\frac {\langle k^{(0)}|V|n^{(0)}\rangle }{E_{n}^{(0)}-E_{k}^{(0)}}}|k^{(0)}\rangle ,$ but the effect on the degenerate states is of $O(\lambda )$ .

Near-degenerate states should also be treated similarly, when the original Hamiltonian splits aren't larger than the perturbation in the near-degenerate subspace. An application is found in the nearly free electron model, where near-degeneracy, treated properly, gives rise to an energy gap even for small perturbations. Other eigenstates will only shift the absolute energy of all near-degenerate states simultaneously.

#### Degeneracy lifted to first order

Let us consider degenerate energy eigenstates and a perturbation that completely lifts the degeneracy to first order of correction.

The perturbed Hamiltonian is denoted as ${\hat {H}}={\hat {H}}_{0}+\lambda {\hat {V}}\,,$ where ${\hat {H}}_{0}$ is the unperturbed Hamiltonian, ${\hat {V}}$ is the perturbation operator, and $0<\lambda <1$ is the parameter of the perturbation.

Let us focus on the degeneracy of the n -th unperturbed energy $E_{n}^{(0)}$ . We will denote the unperturbed states in this degenerate subspace as $\left|\psi _{nk}^{(0)}\right\rangle$ and the other unperturbed states as $\left|\psi _{m}^{(0)}\right\rangle$ , where k is the index of the unperturbed state in the degenerate subspace and $m\neq n$ represents all other energy eigenstates with energies different from $E_{n}^{(0)}$ . The eventual degeneracy among the other states with $\forall m\neq n$ does not change our arguments. All states $\left|\psi _{nk}^{(0)}\right\rangle$ with various values of k share the same energy $E_{n}^{(0)}$ when there is no perturbation, i.e., when $\lambda =0$ . The energies $E_{m}^{(0)}$ of the other states $\left|\psi _{m}^{(0)}\right\rangle$ with $m\neq n$ are all different from $E_{n}^{(0)}$ , but not necessarily unique, i.e. not necessarily always different among themselves.

By $V_{nl,nk}$ and $V_{m,nk}$ , we denote the matrix elements of the perturbation operator ${\hat {V}}$ in the basis of the unperturbed eigenstates. We assume that the basis vectors $\left|\psi _{nk}^{(0)}\right\rangle$ in the degenerate subspace are chosen such that the matrix elements $V_{nl,nk}\equiv \left\langle \psi _{nl}^{(0)}\right|{\hat {V}}\left|\psi _{nk}^{(0)}\right\rangle$ are diagonal. Assuming also that the degeneracy is completely lifted to the first order, i.e. that $E_{nl}^{(1)}\neq E_{nk}^{(1)}$ if $l\neq k$ , we have the following formulae for the energy correction to the second order in $\lambda$ $E_{nk}=E_{n}^{0}+\lambda V_{nk,nk}+\lambda ^{2}\sum \limits _{m\neq n}{\frac {\left|V_{m,nk}\right|^{2}}{E_{n}^{(0)}-E_{m}^{(0)}}}+{\mathcal {O}}(\lambda ^{3})\,,$ and for the state correction to the first order in $\lambda$ $\left|\psi _{nk}\right\rangle =\left|\psi _{nk}^{(0)}\right\rangle +\lambda \sum \limits _{m\neq n}{\frac {V_{m,nk}}{E_{m}^{(0)}-E_{n}^{(0)}}}\left(-\left|\psi _{m}^{(0)}\right\rangle +\sum \limits _{l\neq k}{\frac {V_{nl,m}}{E_{nl}^{(1)}-E_{nk}^{(1)}}}\left|\psi _{nl}^{(0)}\right\rangle \right)+{\mathcal {O}}(\lambda ^{2})\,.$

Notice that here the first order correction to the state is orthogonal to the unperturbed state, $\left\langle \psi _{nk}^{(0)}|\psi _{nk}^{(1)}\right\rangle =0\,.$

### Generalization to multi-parameter case

The generalization of time-independent perturbation theory to the case where there are multiple small parameters $x^{\mu }=(x^{1},x^{2},\cdots )$ in place of λ can be formulated more systematically using the language of differential geometry, which basically defines the derivatives of the quantum states and calculates the perturbative corrections by taking derivatives iteratively at the unperturbed point.

#### Hamiltonian and force operator

From the differential geometric point of view, a parameterized Hamiltonian is considered as a function defined on the parameter manifold that maps each particular set of parameters $(x^{1},x^{2},\cdots )$ to an Hermitian operator *H*(*x μ*) that acts on the Hilbert space. The parameters here can be external field, interaction strength, or driving parameters in the quantum phase transition. Let *En*(*x μ*) and $|n(x^{\mu })\rangle$ be the n-th eigenenergy and eigenstate of *H*(*x μ*) respectively. In the language of differential geometry, the states $|n(x^{\mu })\rangle$ form a vector bundle over the parameter manifold, on which derivatives of these states can be defined. The perturbation theory is to answer the following question: given $E_{n}(x_{0}^{\mu })$ and $|n(x_{0}^{\mu })\rangle$ at an unperturbed reference point $x_{0}^{\mu }$ , how to estimate the *En*(*x μ*) and $|n(x^{\mu })\rangle$ at *x μ* close to that reference point.

Without loss of generality, the coordinate system can be shifted, such that the reference point $x_{0}^{\mu }=0$ is set to be the origin. The following linearly parameterized Hamiltonian is frequently used $H(x^{\mu })=H(0)+x^{\mu }F_{\mu }.$

If the parameters *x μ* are considered as generalized coordinates, then *Fμ* should be identified as the generalized force operators related to those coordinates. Different indices μ label the different forces along different directions in the parameter manifold. For example, if *x μ* denotes the external magnetic field in the μ-direction, then *Fμ* should be the magnetization in the same direction.

#### Perturbation theory as power series expansion

The validity of perturbation theory lies on the adiabatic assumption, which assumes the eigenenergies and eigenstates of the Hamiltonian are smooth functions of parameters such that their values in the vicinity region can be calculated in power series (like Taylor expansion) of the parameters:

${\begin{aligned}E_{n}(x^{\mu })&=E_{n}+x^{\mu }\partial _{\mu }E_{n}+{\frac {1}{2!}}x^{\mu }x^{\nu }\partial _{\mu }\partial _{\nu }E_{n}+\cdots \\[1ex]\left|n(x^{\mu })\right\rangle &=\left|n\right\rangle +x^{\mu }\left|\partial _{\mu }n\right\rangle +{\frac {1}{2!}}x^{\mu }x^{\nu }\left|\partial _{\mu }\partial _{\nu }n\right\rangle +\cdots \end{aligned}}$

Here ∂*μ* denotes the derivative with respect to *x μ*. When applying to the state $|\partial _{\mu }n\rangle$ , it should be understood as the covariant derivative if the vector bundle is equipped with non-vanishing connection. All the terms on the right-hand-side of the series are evaluated at *x μ* = 0, e.g. *En* ≡ *En*(0) and $|n\rangle \equiv |n(0)\rangle$ . This convention will be adopted throughout this subsection, that all functions without the parameter dependence explicitly stated are assumed to be evaluated at the origin. The power series may converge slowly or even not converge when the energy levels are close to each other. The adiabatic assumption breaks down when there is energy level degeneracy, and hence the perturbation theory is not applicable in that case.

#### Hellmann–Feynman theorems

The above power series expansion can be readily evaluated if there is a systematic approach to calculate the derivates to any order. Using the chain rule, the derivatives can be broken down to the single derivative on either the energy or the state. The Hellmann–Feynman theorems are used to calculate these single derivatives. The first Hellmann–Feynman theorem gives the derivative of the energy, $\partial _{\mu }E_{n}=\langle n|\partial _{\mu }H|n\rangle$

The second Hellmann–Feynman theorem gives the derivative of the state (resolved by the complete basis with *m* ≠ *n*), $\langle m|\partial _{\mu }n\rangle ={\frac {\langle m|\partial _{\mu }H|n\rangle }{E_{n}-E_{m}}},\qquad \langle \partial _{\mu }m|n\rangle ={\frac {\langle m|\partial _{\mu }H|n\rangle }{E_{m}-E_{n}}}.$

For the linearly parameterized Hamiltonian, ∂*μ**H* simply stands for the generalized force operator *Fμ*.

The theorems can be simply derived by applying the differential operator ∂*μ* to both sides of the Schrödinger equation $H|n\rangle =E_{n}|n\rangle ,$ which reads

$\partial _{\mu }H|n\rangle +H|\partial _{\mu }n\rangle =\partial _{\mu }E_{n}|n\rangle +E_{n}|\partial _{\mu }n\rangle .$

Then overlap with the state $\langle m|$ from left and make use of the Schrödinger equation $\langle m|H=\langle m|E_{m}$ again,

$\langle m|\partial _{\mu }H|n\rangle +E_{m}\langle m|\partial _{\mu }n\rangle =\partial _{\mu }E_{n}\langle m|n\rangle +E_{n}\langle m|\partial _{\mu }n\rangle .$

Given that the eigenstates of the Hamiltonian always form an orthonormal basis $\langle m|n\rangle =\delta _{mn}$ , the cases of *m* = *n* and *m* ≠ *n* can be discussed separately. The first case will lead to the first theorem and the second case to the second theorem, which can be shown immediately by rearranging the terms. With the differential rules given by the Hellmann–Feynman theorems, the perturbative correction to the energies and states can be calculated systematically.

#### Correction of energy and state

To the second order, the energy correction reads

$E_{n}(x^{\mu })=\langle n|H|n\rangle +\langle n|\partial _{\mu }H|n\rangle x^{\mu }+\Re \sum _{m\neq n}{\frac {\langle n|\partial _{\nu }H|m\rangle \langle m|\partial _{\mu }H|n\rangle }{E_{n}-E_{m}}}x^{\mu }x^{\nu }+\cdots ,$ where $\Re$ denotes the real part function. The first order derivative ∂*μ**En* is given by the first Hellmann–Feynman theorem directly. To obtain the second order derivative ∂*μ*∂*ν**En*, simply applying the differential operator ∂*μ* to the result of the first order derivative $\langle n|\partial _{\nu }H|n\rangle$ , which reads

$\partial _{\mu }\partial _{\nu }E_{n}=\langle \partial _{\mu }n|\partial _{\nu }H|n\rangle +\langle n|\partial _{\mu }\partial _{\nu }H|n\rangle +\langle n|\partial _{\nu }H|\partial _{\mu }n\rangle .$

Note that for a linearly parameterized Hamiltonian, there is no second derivative ∂*μ*∂*ν**H* = 0 on the operator level. Resolve the derivative of state by inserting the complete set of basis, $\partial _{\mu }\partial _{\nu }E_{n}=\sum _{m}\left(\langle \partial _{\mu }n|m\rangle \langle m|\partial _{\nu }H|n\rangle +\langle n|\partial _{\nu }H|m\rangle \langle m|\partial _{\mu }n\rangle \right),$ then all parts can be calculated using the Hellmann–Feynman theorems. In terms of Lie derivatives, $\langle \partial _{\mu }n|n\rangle =\langle n|\partial _{\mu }n\rangle =0$ according to the definition of the connection for the vector bundle. Therefore, the case *m* = *n* can be excluded from the summation, which avoids the singularity of the energy denominator. The same procedure can be carried on for higher order derivatives, from which higher order corrections are obtained.

The same computational scheme is applicable for the correction of states. The result to the second order is as follows ${\begin{aligned}\left|n\left(x^{\mu }\right)\right\rangle =|n\rangle &+\sum _{m\neq n}{\frac {\langle m|\partial _{\mu }H|n\rangle }{E_{n}-E_{m}}}|m\rangle x^{\mu }\\&+\left(\sum _{m\neq n}\sum _{l\neq n}{\frac {\langle m|\partial _{\mu }H|l\rangle \langle l|\partial _{\nu }H|n\rangle }{(E_{n}-E_{m})(E_{n}-E_{l})}}|m\rangle -\sum _{m\neq n}{\frac {\langle m|\partial _{\mu }H|n\rangle \langle n|\partial _{\nu }H|n\rangle }{(E_{n}-E_{m})^{2}}}|m\rangle -{\frac {1}{2}}\sum _{m\neq n}{\frac {\langle n|\partial _{\mu }H|m\rangle \langle m|\partial _{\nu }H|n\rangle }{(E_{n}-E_{m})^{2}}}|n\rangle \right)x^{\mu }x^{\nu }+\cdots .\end{aligned}}$

Both energy derivatives and state derivatives will be involved in deduction. Whenever a state derivative is encountered, resolve it by inserting the complete set of basis, then the Hellmann-Feynman theorem is applicable. Because differentiation can be calculated systematically, the series expansion approach to the perturbative corrections can be coded on computers with symbolic processing software like Mathematica.

#### Effective Hamiltonian

Let *H*(0) be the Hamiltonian completely restricted either in the low-energy subspace ${\mathcal {H}}_{L}$ or in the high-energy subspace ${\mathcal {H}}_{H}$ , such that there is no matrix element in *H*(0) connecting the low- and the high-energy subspaces, i.e. $\langle m|H(0)|l\rangle =0$ if $m\in {\mathcal {H}}_{L},l\in {\mathcal {H}}_{H}$ . Let *Fμ* = ∂*μ**H* be the coupling terms connecting the subspaces. Then when the high energy degrees of freedoms are integrated out, the effective Hamiltonian in the low energy subspace reads

$H_{mn}^{\text{eff}}\left(x^{\mu }\right)=\langle m|H|n\rangle +\delta _{nm}\langle m|\partial _{\mu }H|n\rangle x^{\mu }+{\frac {1}{2!}}\sum _{l\in {\mathcal {H}}_{H}}\left({\frac {\langle m|\partial _{\mu }H|l\rangle \langle l|\partial _{\nu }H|n\rangle }{E_{m}-E_{l}}}+{\frac {\langle m|\partial _{\nu }H|l\rangle \langle l|\partial _{\mu }H|n\rangle }{E_{n}-E_{l}}}\right)x^{\mu }x^{\nu }+\cdots .$

Here $m,n\in {\mathcal {H}}_{L}$ are restricted in the low energy subspace. The above result can be derived by power series expansion of $\langle m|H(x^{\mu })|n\rangle$ .

In a formal way it is possible to define an effective Hamiltonian that gives exactly the low-lying energy states and wavefunctions. In practice, some kind of approximation (perturbation theory) is generally required.
