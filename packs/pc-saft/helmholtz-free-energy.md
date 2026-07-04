---
title: "Helmholtz free energy"
source: https://en.wikipedia.org/wiki/Helmholtz_free_energy
domain: pc-saft
license: CC-BY-SA-4.0
tags: pc-saft
fetched: 2026-07-04
---

# Helmholtz free energy

In thermodynamics, the **Helmholtz free energy** (or **Helmholtz energy**) is a thermodynamic potential that measures the useful work obtainable from a closed thermodynamic system at a constant temperature (isothermal). The change in the Helmholtz energy during a process is equal to the maximum amount of work that the system can perform in a thermodynamic process in which temperature is held constant. At constant temperature, the Helmholtz free energy is minimized at equilibrium.

In contrast, the Gibbs free energy or free enthalpy is most commonly used as a measure of thermodynamic potential (especially in chemistry) when it is convenient for applications that occur at constant *pressure*. For example, in explosives research Helmholtz free energy is often used, since explosive reactions by their nature induce pressure changes. It is also frequently used to define fundamental equations of state of pure substances.

The concept of free energy was developed by Hermann von Helmholtz, a German physicist, and first presented in 1882 in a lecture called "On the thermodynamics of chemical processes". From the German word *Arbeit* (work), the International Union of Pure and Applied Chemistry (IUPAC) recommends the symbol *A* and the name *Helmholtz energy*. In physics, the symbol *F* is also used in reference to *free energy* or *Helmholtz function*.

## Definition

The Helmholtz free energy is defined as $A\equiv U-TS,$ where

- *A* is the Helmholtz free energy (sometimes also called *F*, particularly in the field of physics) (SI: joules, CGS: ergs),
- *U* is the internal energy of the system (SI: joules, CGS: ergs),
- *T* is the absolute temperature (kelvins) of the surroundings, modelled as a heat bath,
- *S* is the entropy of the system (SI: joules per kelvin, CGS: ergs per kelvin).

The Helmholtz energy is the Legendre transformation of the internal energy *U*, in which temperature replaces entropy as the independent variable.

## Formal development

The first law of thermodynamics in a closed system provides $\mathrm {d} U=\delta Q\ +\delta W,$ where U is the internal energy, $\delta Q$ is the energy added as heat, and $\delta W$ is the work done on the system. The second law of thermodynamics for a reversible process yields $\delta Q=T\,\mathrm {d} S$ . In case of a reversible change, the work done can be expressed as $\delta W=-p\,\mathrm {d} V$ (ignoring electrical and other non-*PV* work) and so: $\mathrm {d} U=T\,\mathrm {d} S-p\,\mathrm {d} V.$

Applying the product rule for differentiation to $\mathrm {d} (TS)=T\mathrm {d} S\,+S\mathrm {d} T$ , it follows $\mathrm {d} U=\mathrm {d} (TS)-S\,\mathrm {d} T-p\,\mathrm {d} V,$ and $\mathrm {d} (U-TS)=-S\,\mathrm {d} T-p\,\mathrm {d} V.$

The definition of $A=U-TS$ allows us to rewrite this as $\mathrm {d} A=-S\,\mathrm {d} T-p\,\mathrm {d} V.$

Because *A* is a thermodynamic function of state, this relation is also valid for a process (without electrical work or composition change) that is not reversible.

## Minimum free energy and maximum work principles

The laws of thermodynamics are only directly applicable to systems in thermal equilibrium. If we wish to describe phenomena like chemical reactions, then the best we can do is to consider suitably chosen initial and final states in which the system is in (metastable) thermal equilibrium. If the system is kept at fixed volume and is in contact with a heat bath at some constant temperature, then we can reason as follows.

Since the thermodynamical variables of the system are well defined in the initial state and the final state, the internal energy increase $\Delta U$ , the entropy increase $\Delta S$ , and the total amount of work that can be extracted, performed by the system, W , are well defined quantities. Conservation of energy implies

$\Delta U_{\text{bath}}+\Delta U+W=0.$

The volume of the system is kept constant. This means that the volume of the heat bath does not change either, and we can conclude that the heat bath does not perform any work. This implies that the amount of heat that flows into the heat bath is given by

$Q_{\text{bath}}=\Delta U_{\text{bath}}=-(\Delta U+W).$

The heat bath remains in thermal equilibrium at temperature *T* no matter what the system does. Therefore, the entropy change of the heat bath is

$\Delta S_{\text{bath}}={\frac {Q_{\text{bath}}}{T}}=-{\frac {\Delta U+W}{T}}.$

The total entropy change is thus given by

$\Delta S_{\text{bath}}+\Delta S=-{\frac {\Delta U-T\Delta S+W}{T}}.$

Since the system is in thermal equilibrium with the heat bath in the initial and the final states, *T* is also the temperature of the system in these states. The fact that the system's temperature does not change allows us to express the numerator as the free energy change of the system:

$\Delta S_{\text{bath}}+\Delta S=-{\frac {\Delta A+W}{T}}.$

Since the total change in entropy must always be larger or equal to zero, we obtain the inequality

$W\leq -\Delta A.$

We see that the total amount of work that can be extracted in an isothermal process is limited by the free-energy decrease, and that increasing the free energy in a reversible process requires work to be done on the system. If no work is extracted from the system, then

$\Delta A\leq 0,$

and thus for a system kept at constant temperature and volume and not capable of performing electrical or other non-*PV* work, the total free energy during a spontaneous change can only decrease.

This result seems to contradict the equation $\mathrm {d} A=-S\,\mathrm {d} T-p\,\mathrm {d} V$ , as keeping *T* and *V* constant seems to imply $\mathrm {d} A=0$ , and hence $A=\mathrm {const.}$ In reality there is no contradiction: In a simple one-component system, to which the validity of the equation $\mathrm {d} A=-S\,\mathrm {d} T-p\,\mathrm {d} V$ is restricted, no process can occur at constant *T* and *V*, since there is a unique $P(T,V)$ relation, and thus *T*, *V*, and *P* are all fixed. To allow for spontaneous processes at constant *T* and *V*, one needs to enlarge the thermodynamical state space of the system. In case of a chemical reaction, one must allow for changes in the numbers *N**j* of particles of each type *j*. The differential of the free energy then generalizes to

$\mathrm {d} A=-S\,\mathrm {d} T+P\,\mathrm {d} V+\sum _{j}\mu _{j}\,\mathrm {d} N_{j},$

where the $N_{j}$ are the numbers of particles of type j and the $\mu _{j}$ are the corresponding chemical potentials. This equation is then again valid for both reversible and non-reversible changes. In case of a spontaneous change at constant T and V, the last term will thus be negative.

In case there are other external parameters, the above relation further generalizes to

$\mathrm {d} A=-S\,\mathrm {d} T+P\,\mathrm {d} V-\sum _{i}X_{i}\,\mathrm {d} x_{i}+\sum _{j}\mu _{j}\,\mathrm {d} N_{j}.$

Here the $x_{i}$ are the external variables, and the $X_{i}$ the corresponding generalized forces.

## Relation to the canonical partition function

A system kept at constant volume, temperature, and particle number is described by the canonical ensemble. The probability of finding the system in some energy eigenstate *r*, for any microstate *i*, is given by $P_{r}={\frac {e^{-\beta E_{r}}}{Z}},$ where

- $\beta ={\frac {1}{kT}},$
- $E_{r}$ is the energy of accessible state r
- ${\textstyle Z=\sum _{i}e^{-\beta E_{i}}.}$

*Z* is called the partition function of the system. The fact that the system does not have a unique energy means that the various thermodynamical quantities must be defined as expectation values. In the thermodynamical limit of infinite system size, the relative fluctuations in these averages will go to zero.

The average internal energy of the system is the expectation value of the energy and can be expressed in terms of *Z* as follows:

$U\equiv \langle E\rangle =\sum _{r}P_{r}E_{r}=\sum _{r}{\frac {e^{-\beta E_{r}}E_{r}}{Z}}=\sum _{r}{\frac {-{\frac {\partial }{\partial \beta }}e^{-\beta E_{r}}}{Z}}={\frac {-{\frac {\partial }{\partial \beta }}\sum _{r}e^{-\beta E_{r}}}{Z}}=-{\frac {\partial \log Z}{\partial \beta }}.$

If the system is in state *r*, then the generalized force corresponding to an external variable *x* is given by

$X_{r}=-{\frac {\partial E_{r}}{\partial x}}.$

The thermal average of this can be written as

$X=\sum _{r}P_{r}X_{r}={\frac {1}{\beta }}{\frac {\partial \log Z}{\partial x}}.$

Suppose that the system has one external variable x . Then changing the system's temperature parameter by $d\beta$ and the external variable by $dx$ will lead to a change in $\log Z$ :

$d(\log Z)={\frac {\partial \log Z}{\partial \beta }}\,d\beta +{\frac {\partial \log Z}{\partial x}}\,dx=-U\,d\beta +\beta X\,dx.$

If we write $U\,d\beta$ as

$U\,d\beta =d(\beta U)-\beta \,dU,$

we get

$d(\log Z)=-d(\beta U)+\beta \,dU+\beta X\,dx.$

This means that the change in the internal energy is given by

$dU={\frac {1}{\beta }}\,d(\log Z+\beta U)-X\,dx.$

In the thermodynamic limit, the fundamental thermodynamic relation should hold:

$dU=T\,dS-X\,dx.$

This then implies that the entropy of the system is given by

$S=k\log Z+{\frac {U}{T}}+c,$

where *c* is some constant. The value of *c* can be determined by considering the limit *T* → 0. In this limit the entropy becomes $S=k\log \Omega _{0}$ , where $\Omega _{0}$ is the ground-state degeneracy. The partition function in this limit is $\Omega _{0}e^{-\beta U_{0}}$ , where $U_{0}$ is the ground-state energy. Thus, we see that $c=0$ and that

Microscopic definition of

A

:

$\,A=-kT\log Z.$

### Relating free energy to other variables

Combining the definition of Helmholtz free energy

$A=U-TS$

along with the fundamental thermodynamic relation

$\mathrm {d} A=-S\,\mathrm {d} T-P\,\mathrm {d} V+\mu \,\mathrm {d} N,$

one can find expressions for entropy, pressure and chemical potential:

$S=\left.-\left({\frac {\partial A}{\partial T}}\right)\right|_{V,N},\quad P=\left.-\left({\frac {\partial A}{\partial V}}\right)\right|_{T,N},\quad \mu =\left.\left({\frac {\partial A}{\partial N}}\right)\right|_{T,V}.$

These three equations, along with the free energy in terms of the partition function,

$A=-kT\log Z,$

allow an efficient way of calculating thermodynamic variables of interest given the partition function and are often used in density of state calculations. One can also do Legendre transformations for different systems. For example, for a system with a magnetic field or potential, it is true that

$m=\left.-\left({\frac {\partial A}{\partial B}}\right)\right|_{T,N},\quad V=\left.\left({\frac {\partial A}{\partial Q}}\right)\right|_{N,T}.$

## Bogoliubov inequality

Computing the free energy is an intractable problem for all but the simplest models in statistical physics. A powerful approximation method is mean-field theory, which is a variational method based on the Bogoliubov inequality. This inequality can be formulated as follows.

Suppose we replace the real Hamiltonian H of the model by a trial Hamiltonian ${\tilde {H}}$ , which has different interactions and may depend on extra parameters that are not present in the original model. If we choose this trial Hamiltonian such that

$\left\langle {\tilde {H}}\right\rangle =\langle H\rangle ,$

where both averages are taken with respect to the canonical distribution defined by the trial Hamiltonian ${\tilde {H}}$ , then the Bogoliubov inequality states

$A\leq {\tilde {A}},$

where A is the free energy of the original Hamiltonian, and ${\tilde {A}}$ is the free energy of the trial Hamiltonian. We will prove this below.

By including a large number of parameters in the trial Hamiltonian and minimizing the free energy, we can expect to get a close approximation to the exact free energy.

The Bogoliubov inequality is often applied in the following way. If we write the Hamiltonian as

$H=H_{0}+\Delta H,$

where $H_{0}$ is some exactly solvable Hamiltonian, then we can apply the above inequality by defining

${\tilde {H}}=H_{0}+\langle \Delta H\rangle _{0}.$

Here we have defined $\langle X\rangle _{0}$ to be the average of *X* over the canonical ensemble defined by $H_{0}$ . Since ${\tilde {H}}$ defined this way differs from $H_{0}$ by a constant, we have in general

$\langle X\rangle _{0}=\langle X\rangle .$

where $\langle X\rangle$ is still the average over ${\tilde {H}}$ , as specified above. Therefore,

$\left\langle {\tilde {H}}\right\rangle ={\big \langle }H_{0}+\langle \Delta H\rangle {\big \rangle }=\langle H\rangle ,$

and thus the inequality

$A\leq {\tilde {A}}$

holds. The free energy ${\tilde {A}}$ is the free energy of the model defined by $H_{0}$ plus $\langle \Delta H\rangle$ . This means that

${\tilde {A}}=\langle H_{0}\rangle _{0}-TS_{0}+\langle \Delta H\rangle _{0}=\langle H\rangle _{0}-TS_{0},$

and thus

$A\leq \langle H\rangle _{0}-TS_{0}.$

### Proof of the Bogoliubov inequality

For a classical model we can prove the Bogoliubov inequality as follows. We denote the canonical probability distributions for the Hamiltonian and the trial Hamiltonian by $P_{r}$ and ${\tilde {P}}_{r}$ , respectively. From Gibbs' inequality we know that:

$\sum _{r}{\tilde {P}}_{r}\log \left({\tilde {P}}_{r}\right)\geq \sum _{r}{\tilde {P}}_{r}\log \left(P_{r}\right)\,$

holds. To see this, consider the difference between the left hand side and the right hand side. We can write this as:

$\sum _{r}{\tilde {P}}_{r}\log \left({\frac {{\tilde {P}}_{r}}{P_{r}}}\right)\,$

Since

$\log \left(x\right)\geq 1-{\frac {1}{x}}\,$

it follows that:

$\sum _{r}{\tilde {P}}_{r}\log \left({\frac {{\tilde {P}}_{r}}{P_{r}}}\right)\geq \sum _{r}\left({\tilde {P}}_{r}-P_{r}\right)=0\,$

where in the last step we have used that both probability distributions are normalized to 1.

We can write the inequality as:

$\left\langle \log {\tilde {P}}_{r}\right\rangle \geq \left\langle \log P_{r}\right\rangle$

where the averages are taken with respect to ${\tilde {P}}_{r}$ . If we now substitute in here the expressions for the probability distributions:

$P_{r}={\frac {\exp \left[-\beta H(r)\right]}{Z}}$

and

${\tilde {P}}_{r}={\frac {\exp \left[-\beta {\tilde {H}}(r)\right]}{\tilde {Z}}}$

we get:

$\left\langle -\beta {\tilde {H}}-\log {\tilde {Z}}\right\rangle \geq \left\langle -\beta H-\log Z\right\rangle$

Since the averages of H and ${\tilde {H}}$ are, by assumption, identical we have:

$A\leq {\tilde {A}}$

Here we have used that the partition functions are constants with respect to taking averages and that the free energy is proportional to minus the logarithm of the partition function.

We can easily generalize this proof to the case of quantum mechanical models. We denote the eigenstates of ${\tilde {H}}$ by $\left|r\right\rangle$ . We denote the diagonal components of the density matrices for the canonical distributions for H and ${\tilde {H}}$ in this basis as:

$P_{r}=\left\langle r\left|{\frac {\exp \left[-\beta H\right]}{Z}}\right|r\right\rangle \,$

and

${\tilde {P}}_{r}=\left\langle r\left|{\frac {\exp \left[-\beta {\tilde {H}}\right]}{\tilde {Z}}}\right|r\right\rangle ={\frac {\exp \left(-\beta {\tilde {E}}_{r}\right)}{\tilde {Z}}}\,$

where the ${\tilde {E}}_{r}$ are the eigenvalues of ${\tilde {H}}$

We assume again that the averages of H and ${\tilde {H}}$ in the canonical ensemble defined by ${\tilde {H}}$ are the same:

$\left\langle {\tilde {H}}\right\rangle =\left\langle H\right\rangle \,$

where $\left\langle H\right\rangle =\sum _{r}{\tilde {P}}_{r}\left\langle r\left|H\right|r\right\rangle \,$

The inequality

$\sum _{r}{\tilde {P}}_{r}\log {\tilde {P}}_{r}\geq \sum _{r}{\tilde {P}}_{r}\log P_{r}$

still holds as both the $P_{r}$ and the ${\tilde {P}}_{r}$ sum to 1. On the left-hand side we can replace:

$\log {\tilde {P}}_{r}=-\beta {\tilde {E}}_{r}-\log {\tilde {Z}}$

On the right-hand side we can use the inequality

$\left\langle e^{X}\right\rangle _{r}\geq e^{{\left\langle X\right\rangle }_{r}}$ where we have introduced the notation

$\left\langle Y\right\rangle _{r}\equiv \left\langle r\left|Y\right|r\right\rangle \,$

for the expectation value of the operator Y in the state r. See here for a proof. Taking the logarithm of this inequality gives:

$\log \left[\left\langle e^{X}\right\rangle _{r}\right]\geq \left\langle X\right\rangle _{r}\,$

This allows us to write:

$\log P_{r}=\log \left[\left\langle \exp \left(-\beta H-\log Z\right)\right\rangle _{r}\right]\geq \left\langle -\beta H-\log Z\right\rangle _{r}$

The fact that the averages of H and ${\tilde {H}}$ are the same then leads to the same conclusion as in the classical case:

$A\leq {\tilde {A}}$

## Generalized Helmholtz energy

In the more general case, the mechanical term $p\mathrm {d} V$ must be replaced by the product of volume, stress, and an infinitesimal strain:

$\mathrm {d} A=V\sum _{ij}\sigma _{ij}\,\mathrm {d} \varepsilon _{ij}-S\,\mathrm {d} T+\sum _{i}\mu _{i}\,\mathrm {d} N_{i},$

where $\sigma _{ij}$ is the stress tensor, and $\varepsilon _{ij}$ is the strain tensor. In the case of linear elastic materials that obey Hooke's law, the stress is related to the strain by

$\sigma _{ij}=C_{ijkl}\varepsilon _{kl},$

where we are now using Einstein notation for the tensors, in which repeated indices in a product are summed. We may integrate the expression for $\mathrm {d} A$ to obtain the Helmholtz energy:

${\begin{aligned}A&={\frac {1}{2}}VC_{ijkl}\varepsilon _{ij}\varepsilon _{kl}-ST+\sum _{i}\mu _{i}N_{i}\\&={\frac {1}{2}}V\sigma _{ij}\varepsilon _{ij}-ST+\sum _{i}\mu _{i}N_{i}.\end{aligned}}$

## Application to fundamental equations of state

The Helmholtz free energy function for a pure substance (together with its partial derivatives) can be used to determine all other thermodynamic properties for the substance. See, for example, the equations of state for water, as given by the IAPWS in their IAPWS-95 release.

## Application to training auto-encoders

Hinton and Zemel "derive an objective function for training auto-encoder based on the minimum description length (MDL) principle". "The description length of an input vector using a particular code is the sum of the code cost and reconstruction cost. They define this to be the energy of the code. Given an input vector, they define the energy of a code to be the sum of the code cost and the reconstruction cost." The true expected combined cost is $A=\sum _{i}p_{i}E_{i}-H,$ "which has exactly the form of Helmholtz free energy".
