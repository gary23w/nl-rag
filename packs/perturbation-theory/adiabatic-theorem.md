---
title: "Adiabatic theorem"
source: https://en.wikipedia.org/wiki/Adiabatic_theorem
domain: perturbation-theory
license: CC-BY-SA-4.0
tags: perturbation theory, method of averaging, multiple-scale analysis, adiabatic theorem
fetched: 2026-07-02
---

# Adiabatic theorem

The **adiabatic theorem** is a concept in quantum mechanics. Its original form, due to Max Born and Vladimir Fock (1928), was stated as follows:

A physical system remains in its instantaneous

eigenstate

if a given

perturbation

is acting on it slowly enough and if there is a gap between the

eigenvalue

and the rest of the

Hamiltonian

's

spectrum

.

In simpler terms, a quantum mechanical system subjected to gradually changing external conditions adapts its functional form, but when subjected to rapidly varying conditions there is insufficient time for the functional form to adapt, so the spatial probability density remains unchanged.

## Adiabatic pendulum

At the 1911 Solvay conference, Einstein gave a lecture on the quantum hypothesis, which states that $E=nh\nu$ for atomic oscillators. After Einstein's lecture, Hendrik Lorentz commented that, classically, if a simple pendulum is shortened by holding the wire between two fingers and sliding down, it seems that its energy will change smoothly as the pendulum is shortened. This seems to show that the quantum hypothesis is invalid for macroscopic systems, and if macroscopic systems do not follow the quantum hypothesis, then as the macroscopic system becomes microscopic, it seems the quantum hypothesis would be invalidated. Einstein replied that although both the energy E and the frequency $\nu$ would change, their ratio ${\frac {E}{\nu }}$ would still be conserved, thus saving the quantum hypothesis.

Before the conference, Einstein had just read a paper by Paul Ehrenfest on the adiabatic hypothesis. We know that he had read it because he mentioned it in a letter to Michele Besso written before the conference.

## Diabatic vs. adiabatic processes

| Diabatic | Adiabatic |
|---|---|
| Rapidly changing conditions prevent the system from adapting its configuration during the process, hence the spatial probability density remains unchanged. Typically there is no eigenstate of the final Hamiltonian with the same functional form as the initial state. The system ends in a linear combination of states that sum to reproduce the initial probability density. | Gradually changing conditions allow the system to adapt its configuration, hence the probability density is modified by the process. If the system starts in an eigenstate of the initial Hamiltonian, it will end in the *corresponding* eigenstate of the final Hamiltonian. |

At some initial time $t_{0}$ a quantum-mechanical system has an energy given by the Hamiltonian ${\hat {H}}(t_{0})$ ; the system is in an eigenstate of ${\hat {H}}(t_{0})$ labelled $\psi (x,t_{0})$ . Changing conditions modify the Hamiltonian in a continuous manner, resulting in a final Hamiltonian ${\hat {H}}(t_{1})$ at some later time $t_{1}$ . The system will evolve according to the time-dependent Schrödinger equation, to reach a final state $\psi (x,t_{1})$ . The adiabatic theorem states that the modification to the system depends critically on the time $\tau =t_{1}-t_{0}$ during which the modification takes place.

For a truly adiabatic process we require $\tau \to \infty$ ; in this case the final state $\psi (x,t_{1})$ will be an eigenstate of the final Hamiltonian ${\hat {H}}(t_{1})$ , with a modified configuration:

$|\psi (x,t_{1})|^{2}\neq |\psi (x,t_{0})|^{2}.$

The degree to which a given change approximates an adiabatic process depends on both the energy separation between $\psi (x,t_{0})$ and adjacent states, and the ratio of the interval $\tau$ to the characteristic timescale of the evolution of $\psi (x,t_{0})$ for a time-independent Hamiltonian, $\tau _{\text{int}}=2\pi \hbar /E_{0}$ , where $E_{0}$ is the energy of $\psi (x,t_{0})$ .

Conversely, in the limit $\tau \to 0$ we have infinitely rapid, or diabatic passage; the configuration of the state remains unchanged:

$|\psi (x,t_{1})|^{2}=|\psi (x,t_{0})|^{2}.$

The so-called "gap condition" included in Born and Fock's original definition given above refers to a requirement that the spectrum of ${\hat {H}}$ is discrete and nondegenerate, such that there is no ambiguity in the ordering of the states (one can easily establish which eigenstate of ${\hat {H}}(t_{1})$ *corresponds* to $\psi (t_{0})$ ). In 1999 J. E. Avron and A. Elgart reformulated the adiabatic theorem to adapt it to situations without a gap.

### Comparison with the adiabatic concept in thermodynamics

The term "adiabatic" is traditionally used in thermodynamics to describe processes without the exchange of heat between system and environment (see adiabatic process), more precisely these processes are usually faster than the timescale of heat exchange. (For example, a pressure wave is adiabatic with respect to a heat wave, which is not adiabatic.) Adiabatic in the context of thermodynamics is often used as a synonym for fast process.

The classical and quantum mechanics definition is instead closer to the thermodynamical concept of a quasistatic process, which are processes that are almost always at equilibrium (i.e. that are slower than the internal energy exchange interactions time scales, namely a "normal" atmospheric heat wave is quasi-static, and a pressure wave is not). Adiabatic in the context of mechanics is often used as a synonym for slow process.

In the quantum world adiabatic means for example that the time scale of electrons and photon interactions is much faster or almost instantaneous with respect to the average time scale of electrons and photon propagation. Therefore, we can model the interactions as a piece of continuous propagation of electrons and photons (i.e. states at equilibrium) plus a quantum jump between states (i.e. instantaneous).

The adiabatic theorem in this heuristic context tells essentially that quantum jumps are preferably avoided, and the system tries to conserve the state and the quantum numbers.

The quantum mechanical concept of adiabatic is related to adiabatic invariant, it is often used in the old quantum theory and has no direct relation with heat exchange.

## Example systems

### Simple pendulum

As an example, consider a pendulum oscillating in a vertical plane. If the support is moved, the mode of oscillation of the pendulum will change. If the support is moved *sufficiently slowly*, the motion of the pendulum relative to the support will remain unchanged. A gradual change in external conditions allows the system to adapt, such that it retains its initial character. The detailed classical example is available in the Adiabatic invariant page and here.

### Quantum harmonic oscillator

The classical nature of a pendulum precludes a full description of the effects of the adiabatic theorem. As a further example consider a quantum harmonic oscillator as the spring constant k is increased. Classically this is equivalent to increasing the stiffness of a spring; quantum-mechanically the effect is a narrowing of the potential energy curve in the system Hamiltonian.

If k is increased adiabatically ${\textstyle \left({\frac {dk}{dt}}\to 0\right)}$ then the system at time t will be in an instantaneous eigenstate $\psi (t)$ of the *current* Hamiltonian ${\hat {H}}(t)$ , corresponding to the initial eigenstate of ${\hat {H}}(0)$ . For the special case of a system like the quantum harmonic oscillator described by a single quantum number, this means the quantum number will remain unchanged. **Figure 1** shows how a harmonic oscillator, initially in its ground state, $n=0$ , remains in the ground state as the potential energy curve is compressed; the functional form of the state adapting to the slowly varying conditions.

For a rapidly increased spring constant, the system undergoes a diabatic process ${\textstyle \left({\frac {dk}{dt}}\to \infty \right)}$ in which the system has no time to adapt its functional form to the changing conditions. While the final state must look identical to the initial state $\left(|\psi (t)|^{2}=|\psi (0)|^{2}\right)$ for a process occurring over a vanishing time period, there is no eigenstate of the new Hamiltonian, ${\hat {H}}(t)$ , that resembles the initial state. The final state is composed of a linear superposition of many different eigenstates of ${\hat {H}}(t)$ which sum to reproduce the form of the initial state.

### Avoided curve crossing

For a more widely applicable example, consider a 2-level atom subjected to an external magnetic field. The states, labelled $|1\rangle$ and $|2\rangle$ using bra–ket notation, can be thought of as atomic angular-momentum states, each with a particular geometry. For reasons that will become clear these states will henceforth be referred to as the diabatic states. The system wavefunction can be represented as a linear combination of the diabatic states:

$|\Psi \rangle =c_{1}(t)|1\rangle +c_{2}(t)|2\rangle .$

With the field absent, the energetic separation of the diabatic states is equal to $\hbar \omega _{0}$ ; the energy of state $|1\rangle$ increases with increasing magnetic field (a low-field-seeking state), while the energy of state $|2\rangle$ decreases with increasing magnetic field (a high-field-seeking state). Assuming the magnetic-field dependence is linear, the Hamiltonian matrix for the system with the field applied can be written

$\mathbf {H} ={\begin{pmatrix}\mu B(t)-\hbar \omega _{0}/2&a\\a^{*}&\hbar \omega _{0}/2-\mu B(t)\end{pmatrix}}$

where $\mu$ is the magnetic moment of the atom, assumed to be the same for the two diabatic states, and a is some time-independent coupling between the two states. The diagonal elements are the energies of the diabatic states ( $E_{1}(t)$ and $E_{2}(t)$ ), however, as $\mathbf {H}$ is not a diagonal matrix, it is clear that these states are not eigenstates of $\mathbf {H}$ due to the off-diagonal coupling constant.

The eigenvectors of the matrix $\mathbf {H}$ are the eigenstates of the system, which we will label $|\phi _{1}(t)\rangle$ and $|\phi _{2}(t)\rangle$ , with corresponding eigenvalues ${\begin{aligned}\varepsilon _{1}(t)&=-{\frac {1}{2}}{\sqrt {4a^{2}+(\hbar \omega _{0}-2\mu B(t))^{2}}}\\[4pt]\varepsilon _{2}(t)&=+{\frac {1}{2}}{\sqrt {4a^{2}+(\hbar \omega _{0}-2\mu B(t))^{2}}}.\end{aligned}}$

It is important to realise that the eigenvalues $\varepsilon _{1}(t)$ and $\varepsilon _{2}(t)$ are the only allowed outputs for any individual measurement of the system energy, whereas the diabatic energies $E_{1}(t)$ and $E_{2}(t)$ correspond to the expectation values for the energy of the system in the diabatic states $|1\rangle$ and $|2\rangle$ .

**Figure 2** shows the dependence of the diabatic and adiabatic energies on the value of the magnetic field; note that for non-zero coupling the eigenvalues of the Hamiltonian cannot be degenerate, and thus we have an avoided crossing. If an atom is initially in state $|\phi _{2}(t_{0})\rangle$ in zero magnetic field (on the red curve, at the extreme left), an adiabatic increase in magnetic field ${\textstyle \left({\frac {dB}{dt}}\to 0\right)}$ will ensure the system remains in an eigenstate of the Hamiltonian $|\phi _{2}(t)\rangle$ throughout the process (follows the red curve). A diabatic increase in magnetic field ${\textstyle \left({\frac {dB}{dt}}\to \infty \right)}$ will ensure the system follows the diabatic path (the dotted blue line), such that the system undergoes a transition to state $|\phi _{1}(t_{1})\rangle$ . For finite magnetic field slew rates ${\textstyle \left(0<{\frac {dB}{dt}}<\infty \right)}$ there will be a finite probability of finding the system in either of the two eigenstates. See below for approaches to calculating these probabilities.

These results are extremely important in atomic and molecular physics for control of the energy-state distribution in a population of atoms or molecules.

## Mathematical statement

Under a slowly changing Hamiltonian $H(t)$ with instantaneous eigenstates $|n(t)\rangle$ and corresponding energies $E_{n}(t)$ , a quantum system evolves from the initial state $|\psi (0)\rangle =\sum _{n}c_{n}(0)|n(0)\rangle$ to the final state $|\psi (t)\rangle =\sum _{n}c_{n}(t)|n(t)\rangle ,$ where the coefficients undergo the change of phase $c_{n}(t)=c_{n}(0)e^{i\theta _{n}(t)}e^{i\gamma _{n}(t)}$

with the **dynamical phase** $\theta _{m}(t)=-{\frac {1}{\hbar }}\int _{0}^{t}E_{m}(t')dt'$

and **geometric phase** $\gamma _{m}(t)=i\int _{0}^{t}\langle m(t')|{\dot {m}}(t')\rangle dt'.$

In particular, $|c_{n}(t)|^{2}=|c_{n}(0)|^{2}$ , so if the system begins in an eigenstate of $H(0)$ , it remains in an eigenstate of $H(t)$ during the evolution with a change of phase only.

### Proofs

| Sakurai in *Modern Quantum Mechanics* |
|---|
| This proof is partly inspired by one given by Sakurai in *Modern Quantum Mechanics*. The instantaneous eigenstates $\|n(t)\rangle$ and energies $E_{n}(t)$ , by assumption, satisfy the time-independent Schrödinger equation $H(t)\|n(t)\rangle =E_{n}(t)\|n(t)\rangle$ at all times t . Thus, they constitute a basis that can be used to expand the state $\|\psi (t)\rangle =\sum _{n}c_{n}(t)\|n(t)\rangle$ at any time t . The evolution of the system is governed by the time-dependent Schrödinger equation $i\hbar \|{\dot {\psi }}(t)\rangle =H(t)\|\psi (t)\rangle ,$ where ${\dot {}}=d/dt$ (see Notation for differentiation § Newton's notation). Insert the expansion of $\|\psi (t)\rangle$ , use $H(t)\|n(t)\rangle =E_{n}(t)\|n(t)\rangle$ , differentiate with the product rule, take the inner product with $\|m(t)\rangle$ and use orthonormality of the eigenstates to obtain $i\hbar {\dot {c}}_{m}(t)+i\hbar \sum _{n}c_{n}(t)\langle m(t)\|{\dot {n}}(t)\rangle =c_{m}(t)E_{m}(t).$ This coupled first-order differential equation is exact and expresses the time-evolution of the coefficients in terms of inner products $\langle m(t)\|{\dot {n}}(t)\rangle$ between the eigenstates and the time-differentiated eigenstates. But it is possible to re-express the inner products for $m\neq n$ in terms of matrix elements of the time-differentiated Hamiltonian ${\dot {H}}(t)$ . To do so, differentiate both sides of the time-independent Schrödinger equation with respect to time using the product rule to get ${\dot {H}}(t)\|n(t)\rangle +H(t)\|{\dot {n}}(t)\rangle ={\dot {E}}_{n}(t)\|n(t)\rangle +E_{n}(t)\|{\dot {n}}(t)\rangle .$ Again take the inner product with $\|m(t)\rangle$ and use $\langle m(t)\|H(t)=E_{m}(t)\langle m(t)\|$ and orthonormality to find $\langle m(t)\|{\dot {n}}(t)\rangle =-{\frac {\langle m(t)\|{\dot {H}}(t)\|n(t)\rangle }{E_{m}(t)-E_{n}(t)}}\qquad (m\neq n).$ Insert this into the differential equation for the coefficients to obtain ${\dot {c}}_{m}(t)+\left({\frac {i}{\hbar }}E_{m}(t)+\langle m(t)\|{\dot {m}}(t)\rangle \right)c_{m}(t)=\sum _{n\neq m}{\frac {\langle m(t)\|{\dot {H}}\|n(t)\rangle }{E_{m}(t)-E_{n}(t)}}c_{n}(t).$ This differential equation describes the time-evolution of the coefficients, but now in terms of matrix elements of ${\dot {H}}(t)$ . To arrive at the adiabatic theorem, neglect the right hand side. This is valid if the rate of change of the Hamiltonian ${\dot {H}}(t)$ is small **and** there is a finite gap $E_{m}(t)-E_{n}(t)\neq 0$ between the energies. This is known as the **adiabatic approximation**. Under the adiabatic approximation, ${\dot {c}}_{m}(t)=i\left(-{\frac {E_{m}(t)}{\hbar }}+i\langle m(t)\|{\dot {m}}(t)\rangle \right)c_{m}(t)$ which integrates precisely to the adiabatic theorem $c_{m}(t)=c_{m}(0)e^{i\theta _{m}(t)}e^{i\gamma _{m}(t)}$ with the phases defined in the statement of the theorem. The dynamical phase $\theta _{m}(t)$ is real because it involves an integral over a real energy. To see that the geometric phase $\gamma _{m}(t)$ is purely real, differentiate the normalization $\langle m(t)\|m(t)\rangle =1$ of the eigenstates and use the product rule to find that $0={\frac {d}{dt}}{\Bigl (}\langle m(t)\|m(t)\rangle {\Bigr )}=\langle {\dot {m}}(t)\|m(t)\rangle +\langle m(t))\|{\dot {m}}(t)\rangle =\langle m(t))\|{\dot {m}}(t)\rangle ^{*}+\langle m(t))\|{\dot {m}}(t)\rangle =2\,\operatorname {Re} {\Bigl (}\langle m(t))\|{\dot {m}}(t)\rangle {\Bigr )}.$ Thus, $\langle m(t))\|{\dot {m}}(t)\rangle$ is purely imaginary, so the geometric phase $\gamma _{m}(t)$ is purely real. |

| Adiabatic approximation |
|---|
| Proof with the details of the adiabatic approximation We are going to formulate the statement of the theorem as follows: For a slowly varying Hamiltonian ${\hat {H}}$ in the time range T the solution of the Schrödinger equation $\Psi (t)$ with initial conditions $\Psi (0)=\psi _{n}(0)$ where $\psi _{n}(t)$ is the eigenvector of the instantaneous Schrödinger equation ${\hat {H}}(t)\psi _{n}(t)=E_{n}(t)\psi _{n}(t)$ can be approximated as: $\left\\|{\Psi (t)-\psi _{\text{adiabatic}}(t)}\right\\|\approx O(T^{-1})$ where the adiabatic approximation is: $\|\psi _{\text{adiabatic}}(t)\rangle =e^{i\theta _{n}(t)}e^{i\gamma _{n}(t)}\|\psi _{n}(t)\rangle$ and $\theta _{n}(t)=-{\frac {1}{\hbar }}\int _{0}^{t}E_{n}(t')dt'$ $\gamma _{n}(t)=\int _{0}^{t}\nu _{n}(t')dt'$ also called Berry phase $\nu _{n}(t)=i\langle \psi _{n}(t)\|{\dot {\psi }}_{n}(t)\rangle$ And now we are going to prove the theorem. Consider the *time-dependent* Schrödinger equation $i\hbar {\partial \over \partial t}\|\psi (t)\rangle ={\hat {H}}({\tfrac {t}{T}})\|\psi (t)\rangle$ with Hamiltonian ${\hat {H}}(t).$ We would like to know the relation between an initial state $\|\psi (0)\rangle$ and its final state $\|\psi (T)\rangle$ at $t=T$ in the adiabatic limit $T\to \infty .$ First redefine time as $\lambda ={\tfrac {t}{T}}\in [0,1]$ : $i\hbar {\partial \over \partial \lambda }\|\psi (\lambda )\rangle =T{\hat {H}}(\lambda )\|\psi (\lambda )\rangle .$ At every point in time ${\hat {H}}(\lambda )$ can be diagonalized ${\hat {H}}(\lambda )\|\psi _{n}(\lambda )\rangle =E_{n}(\lambda )\|\psi _{n}(\lambda )\rangle$ with eigenvalues $E_{n}$ and eigenvectors $\|\psi _{n}(\lambda )\rangle$ . Since the eigenvectors form a complete basis at any time we can expand $\|\psi (\lambda )\rangle$ as: $\|\psi (\lambda )\rangle =\sum _{n}c_{n}(\lambda )\|\psi _{n}(\lambda )\rangle e^{iT\theta _{n}(\lambda )},$ where $\theta _{n}(\lambda )=-{\frac {1}{\hbar }}\int _{0}^{\lambda }E_{n}(\lambda ')d\lambda '.$ The phase $\theta _{n}(t)$ is called the *dynamic phase factor*. By substitution into the Schrödinger equation, another equation for the variation of the coefficients can be obtained: $i\hbar \sum _{n}({\dot {c}}_{n}\|\psi _{n}\rangle +c_{n}\|{\dot {\psi }}_{n}\rangle +ic_{n}\|\psi _{n}\rangle T{\dot {\theta }}_{n})e^{iT\theta _{n}}=\sum _{n}c_{n}TE_{n}\|\psi _{n}\rangle e^{iT\theta _{n}}.$ The term ${\dot {\theta }}_{n}$ gives $-E_{n}/\hbar$ , and so the third term of left side cancels out with the right side, leaving $\sum _{n}{\dot {c}}_{n}\|\psi _{n}\rangle e^{iT\theta _{n}}=-\sum _{n}c_{n}\|{\dot {\psi }}_{n}\rangle e^{iT\theta _{n}}.$ Now taking the inner product with an arbitrary eigenfunction $\langle \psi _{m}\|$ , the $\langle \psi _{m}\|\psi _{n}\rangle$ on the left gives $\delta _{nm}$ , which is 1 only for *m* = *n* and otherwise vanishes. The remaining part gives ${\dot {c}}_{m}=-\sum _{n}c_{n}\langle \psi _{m}\|{\dot {\psi }}_{n}\rangle e^{iT(\theta _{n}-\theta _{m})}.$ For $T\to \infty$ the $e^{iT(\theta _{n}-\theta _{m})}$ will oscillate faster and faster and intuitively will eventually suppress nearly all terms on the right side. The only exceptions are when $\theta _{n}-\theta _{m}$ has a critical point, i.e. $E_{n}(\lambda )=E_{m}(\lambda )$ . This is trivially true for $m=n$ . Since the adiabatic theorem assumes a gap between the eigenenergies at any time this cannot hold for $m\neq n$ . Therefore, only the $m=n$ term will remain in the limit $T\to \infty$ . In order to show this more rigorously we first need to remove the $m=n$ term. This can be done by defining $d_{m}(\lambda )=c_{m}(\lambda )e^{\int _{0}^{\lambda }\langle \psi _{m}\|{\dot {\psi }}_{m}\rangle d\lambda }=c_{m}(\lambda )e^{-i\gamma _{m}(\lambda )}.$ We obtain: ${\dot {d}}_{m}=-\sum _{n\neq m}d_{n}\langle \psi _{m}\|{\dot {\psi }}_{n}\rangle e^{iT(\theta _{n}-\theta _{m})-i(\gamma _{m}-\gamma _{n})}.$ This equation can be integrated: ${\begin{aligned}d_{m}(1)-d_{m}(0)&=-\int _{0}^{1}\sum _{n\neq m}d_{n}\langle \psi _{m}\|{\dot {\psi }}_{n}\rangle e^{iT(\theta _{n}-\theta _{m})-i(\gamma _{m}-\gamma _{n})}d\lambda \\&=-\int _{0}^{1}\sum _{n\neq m}(d_{n}-d_{n}(0))\langle \psi _{m}\|{\dot {\psi }}_{n}\rangle e^{iT(\theta _{n}-\theta _{m})-i(\gamma _{m}-\gamma _{n})}d\lambda -\int _{0}^{1}\sum _{n\neq m}d_{n}(0)\langle \psi _{m}\|{\dot {\psi }}_{n}\rangle e^{iT(\theta _{n}-\theta _{m})-i(\gamma _{m}-\gamma _{n})}d\lambda \end{aligned}}$ or written in vector notation ${\vec {d}}(1)-{\vec {d}}(0)=-\int _{0}^{1}{\hat {A}}(T,\lambda )({\vec {d}}(\lambda )-{\vec {d}}(0))d\lambda -{\vec {\alpha }}(T).$ Here ${\hat {A}}(T,\lambda )$ is a matrix and $\alpha _{m}(T)=\int _{0}^{1}\sum _{n\neq m}d_{n}(0)\langle \psi _{m}\|{\dot {\psi }}_{n}\rangle e^{iT(\theta _{n}-\theta _{m})-i(\gamma _{m}-\gamma _{n})}d\lambda$ is basically a Fourier transform. It follows from the Riemann-Lebesgue lemma that ${\vec {\alpha }}(T)\to 0$ as $T\to \infty$ . As last step take the norm on both sides of the above equation: $\Vert {\vec {d}}(1)-{\vec {d}}(0)\Vert \leq \Vert {\vec {\alpha }}(T)\Vert +\int _{0}^{1}\Vert {\hat {A}}(T,\lambda )\Vert \Vert {\vec {d}}(\lambda )-{\vec {d}}(0)\Vert d\lambda$ and apply Grönwall's inequality to obtain $\Vert {\vec {d}}(1)-{\vec {d}}(0)\Vert \leq \Vert {\vec {\alpha }}(T)\Vert e^{\int _{0}^{1}\Vert {\hat {A}}(T,\lambda )\Vert d\lambda }.$ Since ${\vec {\alpha }}(T)\to 0$ it follows $\Vert {\vec {d}}(1)-{\vec {d}}(0)\Vert \to 0$ for $T\to \infty$ . This concludes the proof of the adiabatic theorem. In the adiabatic limit the eigenstates of the Hamiltonian evolve independently of each other. If the system is prepared in an eigenstate $\|\psi (0)\rangle =\|\psi _{n}(0)\rangle$ its time evolution is given by: $\|\psi (\lambda )\rangle =\|\psi _{n}(\lambda )\rangle e^{iT\theta _{n}(\lambda )}e^{i\gamma _{n}(\lambda )}.$ So, for an adiabatic process, a system starting from *n*th eigenstate also remains in that *n*th eigenstate like it does for the time-independent processes, only picking up a couple of phase factors. The new phase factor $\gamma _{n}(t)$ can be canceled out by an appropriate choice of gauge for the eigenfunctions. However, if the adiabatic evolution is cyclic, then $\gamma _{n}(t)$ becomes a gauge-invariant physical quantity, known as the Berry phase. |

| Generic proof in parameter space |
|---|
| Let's start from a parametric Hamiltonian $H({\vec {R}}(t))$ , where the parameters are slowly varying in time, the definition of slow here is defined essentially by the distance in energy by the eigenstates (through the uncertainty principle, we can define a timescale that shall be always much lower than the time scale considered). This way we clearly also identify that while slowly varying the eigenstates remains clearly separated in energy (e.g. also when we generalize this to the case of bands as in the TKNN formula the bands shall remain clearly separated). Given they do not intersect the states are ordered and in this sense this is also one of the meanings of the name topological order. We do have the instantaneous Schrödinger equation: $H({\vec {R}}(t))\|\psi _{m}(t)\rangle =E_{m}(t)\|\psi _{m}(t)\rangle$ And instantaneous eigenstates: $\langle \psi _{m}(t)\|\psi _{n}(t)\rangle =\delta _{mn}$ The generic solution: $\|\Psi (t)\rangle =\sum a_{n}(t)\|\psi _{n}(t)\rangle$ plugging in the full Schrödinger equation and multiplying by a generic eigenvector: $\langle \psi _{m}(t)\|i\hbar \partial _{t}\|\Psi (t)\rangle =\langle \psi _{m}(t)\|H({\vec {R}}(t))\|\Psi (t)\rangle$ ${\dot {a}}_{m}+\sum _{n}\langle \psi _{m}(t)\|\partial _{\vec {R}}\|\psi _{n}(t)\rangle {\dot {\vec {R}}}a_{n}=-{\frac {i}{\hbar }}E_{m}(t)a_{m}$ And if we introduce the adiabatic approximation: $\|\langle \psi _{m}(t)\|\partial _{\vec {R}}\|\psi _{n}(t)\rangle {\dot {\vec {R}}}a_{n}\|\ll \|a_{m}\|$ for each $m\neq n$ We have ${\dot {a}}_{m}=-\langle \psi _{m}(t)\|\partial _{\vec {R}}\|\psi _{m}(t)\rangle {\dot {\vec {R}}}a_{m}-{\frac {i}{\hbar }}E_{m}(t)a_{m}$ and $a_{m}(t)=e^{-{\frac {i}{\hbar }}\int _{t_{0}}^{t}E_{m}(t')dt'}e^{i\gamma _{m}(t)}a_{m}(t_{0})$ where $\gamma _{m}(t)=i\int _{t_{0}}^{t}\langle \psi _{m}(t)\|\partial _{\vec {R}}\|\psi _{m}(t)\rangle {\dot {\vec {R}}}dt'=i\int _{C}\langle \psi _{m}({\vec {R}})\|\partial _{\vec {R}}\|\psi _{m}({\vec {R}})\rangle d{\vec {R}}$ And C is the path in the parameter space, This is the same as the statement of the theorem but in terms of the coefficients of the total wave function and its initial state. Now this is slightly more general than the other proofs given we consider a generic set of parameters, and we see that the Berry phase acts as a local geometric quantity in the parameter space. Finally integrals of local geometric quantities can give topological invariants as in the case of the Gauss-Bonnet theorem. In fact if the path C is closed then the Berry phase persists to gauge transformation and becomes a physical quantity. |

## Example applications

Often a solid crystal is modeled as a set of independent valence electrons moving in a mean perfectly periodic potential generated by a rigid lattice of ions. With the Adiabatic theorem we can also include instead the motion of the valence electrons across the crystal and the thermal motion of the ions as in the Born–Oppenheimer approximation.

This does explain many phenomena in the scope of:

- **thermodynamics**: Temperature dependence of specific heat, thermal expansion, melting
- **transport phenomena**: the temperature dependence of electric resistivity of conductors, the temperature dependence of electric conductivity in insulators, Some properties of low temperature superconductivity
- **optics**: optic absorption in the infrared for ionic crystals, Brillouin scattering, Raman scattering

## Deriving conditions for diabatic vs adiabatic passage

We will now pursue a more rigorous analysis. Making use of bra–ket notation, the state vector of the system at time t can be written

$|\psi (t)\rangle =\sum _{n}c_{n}^{A}(t)e^{-iE_{n}t/\hbar }|\phi _{n}\rangle ,$

where the spatial wavefunction alluded to earlier is the projection of the state vector onto the eigenstates of the position operator

$\psi (x,t)=\langle x|\psi (t)\rangle .$

It is instructive to examine the limiting cases, in which $\tau$ is very large (adiabatic, or gradual change) and very small (diabatic, or sudden change).

Consider a system Hamiltonian undergoing continuous change from an initial value ${\hat {H}}_{0}$ , at time $t_{0}$ , to a final value ${\hat {H}}_{1}$ , at time $t_{1}$ , where $\tau =t_{1}-t_{0}$ . The evolution of the system can be described in the Schrödinger picture by the time-evolution operator, defined by the integral equation

${\hat {U}}(t,t_{0})=1-{\frac {i}{\hbar }}\int _{t_{0}}^{t}{\hat {H}}(t'){\hat {U}}(t',t_{0})dt',$

which is equivalent to the Schrödinger equation.

$i\hbar {\frac {\partial }{\partial t}}{\hat {U}}(t,t_{0})={\hat {H}}(t){\hat {U}}(t,t_{0}),$

along with the initial condition ${\hat {U}}(t_{0},t_{0})=1$ . Given knowledge of the system wave function at $t_{0}$ , the evolution of the system up to a later time t can be obtained using

$|\psi (t)\rangle ={\hat {U}}(t,t_{0})|\psi (t_{0})\rangle .$

The problem of determining the *adiabaticity* of a given process is equivalent to establishing the dependence of ${\hat {U}}(t_{1},t_{0})$ on $\tau$ .

To determine the validity of the adiabatic approximation for a given process, one can calculate the probability of finding the system in a state other than that in which it started. Using bra–ket notation and using the definition $|0\rangle \equiv |\psi (t_{0})\rangle$ , we have:

$\zeta =\langle 0|{\hat {U}}^{\dagger }(t_{1},t_{0}){\hat {U}}(t_{1},t_{0})|0\rangle -\langle 0|{\hat {U}}^{\dagger }(t_{1},t_{0})|0\rangle \langle 0|{\hat {U}}(t_{1},t_{0})|0\rangle .$

We can expand ${\hat {U}}(t_{1},t_{0})$

${\hat {U}}(t_{1},t_{0})=1+{1 \over i\hbar }\int _{t_{0}}^{t_{1}}{\hat {H}}(t)dt+{1 \over (i\hbar )^{2}}\int _{t_{0}}^{t_{1}}dt'\int _{t_{0}}^{t'}dt''{\hat {H}}(t'){\hat {H}}(t'')+\cdots .$

In the perturbative limit we can take just the first two terms and substitute them into our equation for $\zeta$ , recognizing that

${1 \over \tau }\int _{t_{0}}^{t_{1}}{\hat {H}}(t)dt\equiv {\bar {H}}$

is the system Hamiltonian, averaged over the interval $t_{0}\to t_{1}$ , we have:

$\zeta =\langle 0|(1+{\tfrac {i}{\hbar }}\tau {\bar {H}})(1-{\tfrac {i}{\hbar }}\tau {\bar {H}})|0\rangle -\langle 0|(1+{\tfrac {i}{\hbar }}\tau {\bar {H}})|0\rangle \langle 0|(1-{\tfrac {i}{\hbar }}\tau {\bar {H}})|0\rangle .$

After expanding the products and making the appropriate cancellations, we are left with:

$\zeta ={\frac {\tau ^{2}}{\hbar ^{2}}}\left(\langle 0|{\bar {H}}^{2}|0\rangle -\langle 0|{\bar {H}}|0\rangle \langle 0|{\bar {H}}|0\rangle \right),$

giving

$\zeta ={\frac {\tau ^{2}\Delta {\bar {H}}^{2}}{\hbar ^{2}}},$

where $\Delta {\bar {H}}$ is the root mean square deviation of the system Hamiltonian averaged over the interval of interest.

The sudden approximation is valid when $\zeta \ll 1$ (the probability of finding the system in a state other than that in which is started approaches zero), thus the validity condition is given by

$\tau \ll {\hbar \over \Delta {\bar {H}}},$

which is a statement of the time-energy form of the Heisenberg uncertainty principle.

### Diabatic passage

In the limit $\tau \to 0$ we have infinitely rapid, or diabatic passage:

$\lim _{\tau \to 0}{\hat {U}}(t_{1},t_{0})=1.$

The functional form of the system remains unchanged:

$|\langle x|\psi (t_{1})\rangle |^{2}=\left|\langle x|\psi (t_{0})\rangle \right|^{2}.$

This is sometimes referred to as the sudden approximation. The validity of the approximation for a given process can be characterized by the probability that the state of the system remains unchanged:

$P_{D}=1-\zeta .$

### Adiabatic passage

In the limit $\tau \to \infty$ we have infinitely slow, or adiabatic passage. The system evolves, adapting its form to the changing conditions,

$|\langle x|\psi (t_{1})\rangle |^{2}\neq |\langle x|\psi (t_{0})\rangle |^{2}.$

If the system is initially in an eigenstate of ${\hat {H}}(t_{0})$ , after a period $\tau$ it will have passed into the *corresponding* eigenstate of ${\hat {H}}(t_{1})$ .

This is referred to as the adiabatic approximation. The validity of the approximation for a given process can be determined from the probability that the final state of the system is different from the initial state:

$P_{A}=\zeta .$

## Calculating adiabatic passage probabilities

### The Landau–Zener formula

In 1932 an analytic solution to the problem of calculating adiabatic transition probabilities was published separately by Lev Landau and Clarence Zener, for the special case of a linearly changing perturbation in which the time-varying component does not couple the relevant states (hence the coupling in the diabatic Hamiltonian matrix is independent of time).

The key figure of merit in this approach is the Landau–Zener velocity: $v_{\text{LZ}}={{\frac {\partial }{\partial t}}|E_{2}-E_{1}| \over {\frac {\partial }{\partial q}}|E_{2}-E_{1}|}\approx {\frac {dq}{dt}},$ where q is the perturbation variable (electric or magnetic field, molecular bond-length, or any other perturbation to the system), and $E_{1}$ and $E_{2}$ are the energies of the two diabatic (crossing) states. A large $v_{\text{LZ}}$ results in a large diabatic transition probability and vice versa.

Using the Landau–Zener formula the probability, $P_{\rm {D}}$ , of a diabatic transition is given by

${\begin{aligned}P_{\rm {D}}&=e^{-2\pi \Gamma }\\\Gamma &={a^{2}/\hbar \over \left|{\frac {\partial }{\partial t}}(E_{2}-E_{1})\right|}={a^{2}/\hbar \over \left|{\frac {dq}{dt}}{\frac {\partial }{\partial q}}(E_{2}-E_{1})\right|}\\&={a^{2} \over \hbar |\alpha |}\\\end{aligned}}$

### The numerical approach

For a transition involving a nonlinear change in perturbation variable or time-dependent coupling between the diabatic states, the equations of motion for the system dynamics cannot be solved analytically. The diabatic transition probability can still be obtained using one of the wide varieties of numerical solution algorithms for ordinary differential equations.

The equations to be solved can be obtained from the time-dependent Schrödinger equation:

$i\hbar {\dot {\underline {c}}}^{A}(t)=\mathbf {H} _{A}(t){\underline {c}}^{A}(t),$

where ${\underline {c}}^{A}(t)$ is a vector containing the adiabatic state amplitudes, $\mathbf {H} _{A}(t)$ is the time-dependent adiabatic Hamiltonian, and the overdot represents a time derivative.

Comparison of the initial conditions used with the values of the state amplitudes following the transition can yield the diabatic transition probability. In particular, for a two-state system: $P_{D}=|c_{2}^{A}(t_{1})|^{2}$ for a system that began with $|c_{1}^{A}(t_{0})|^{2}=1$ .
