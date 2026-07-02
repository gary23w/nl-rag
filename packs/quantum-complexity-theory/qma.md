---
title: "QMA - Wikipedia"
source: https://en.wikipedia.org/wiki/QMA
domain: quantum-complexity-theory
license: CC-BY-SA-4.0
tags: quantum complexity theory, quantum query complexity, quantum supremacy, qma class
fetched: 2026-07-02
---

# QMA

**QMA**, as an abbreviation for **Quantum Merlin Arthur,** refers to a complexity class in computational complexity theory. It is the set of all formal languages that satisfy the following properties:

1. If a string is in the language, then there is a polynomial-size quantum proof (representable as a quantum state) that convinces a polynomial-time quantum verifier (running on a quantum computer) of this fact with high probability.
2. If a string is *not* in the language, every polynomial-size quantum state is rejected by the verifier with high probability.

The relationship between QMA and BQP is analogous to the relationship between the complexity classes NP and P. It is also analogous to the relationship between the probabilistic complexity classes MA and BPP.

**QAM** is a related complexity class, in which fictional agents Arthur and Merlin carry out the sequence: Arthur generates a random string, Merlin answers with a quantum certificate and Arthur verifies it as a BQP machine.

## Definition

A language *L* is in ${\mathsf {QMA}}(c,s)$ if there exists a polynomial time quantum verifier *V* and a polynomial ⁠ $p(x)$ ⁠ such that:

- $\forall x\in L$ , there exists a quantum state $|\psi \rangle$ such that the probability that *V* accepts the input $(|x\rangle ,|\psi \rangle )$ is greater than c.
- $\forall x\notin L$ , and for all quantum states $|\psi \rangle$ with at most $p(|x|)$ qubits, the probability that *V* accepts the input $(|x\rangle ,|\psi \rangle )$ is less than s.

The complexity class ${\mathsf {QMA}}$ is defined to be equal to ${\mathsf {QMA}}({2}/{3},1/3)$ . However, the constants are not too important since the class remains unchanged if c and s are set to any constants such that c is greater than s. Moreover, for any polynomials $q(n)$ and $r(n)$ , we have

${\mathsf {QMA}}\left({\frac {2}{3}},{\frac {1}{3}}\right)={\mathsf {QMA}}\left({\frac {1}{2}}+{\frac {1}{q(n)}},{\frac {1}{2}}-{\frac {1}{q(n)}}\right)={\mathsf {QMA}}(1-2^{-r(n)},2^{-r(n)})$

.

## Problems in QMA

Since many interesting classes are contained in QMA, such as P, BQP and NP, all problems in those classes are also in QMA. However, there are problems that are in QMA but not known to be in NP or BQP. Some such well known problems are discussed below.

A problem is said to be QMA-hard, analogous to NP-hard, if every problem in QMA can be reduced to it. A problem is said to be QMA-complete if it is QMA-hard and in QMA.

### The local Hamiltonian problem

A *k*-local Hamiltonian (quantum mechanics) H is a Hermitian matrix acting on n qubits which can be represented as the sum of m Hamiltonian Terms acting upon at most k qubits each.

$H=\sum _{i=1}^{m}H_{i}$

The general *k*-local Hamiltonian problem is, given a *k*-local Hamiltonian H , to find the smallest eigenvalue $\lambda$ of H . $\lambda$ is also called the ground state energy of the Hamiltonian.

The decision version of the *k*-local Hamiltonian problem is a type of promise problem and is defined as, given a *k*-local Hamiltonian and $\alpha ,\beta$ where $\alpha >\beta$ , to decide if there exists a quantum eigenstate $|\psi \rangle$ of H with associated eigenvalue $\lambda$ , such that $\lambda \leq \beta$ or if $\lambda \geq \alpha$ .

The local Hamiltonian problem is the quantum analogue of MAX-SAT. The *k*-local Hamiltonian problem is QMA-complete for k ≥ 2.

The 2-local Hamiltonian problem restricted to act on a two dimensional grid of qubits, is also QMA-complete. It has been shown that the *k*-local Hamiltonian problem is still QMA-hard even for Hamiltonians representing a 1-dimensional line of particles with nearest-neighbor interactions with 12 states per particle. If the system is translationally-invariant, its local Hamiltonian problem becomes QMAEXP-complete (as the problem input is encoded in the system size, the verifier now has exponential runtime while maintaining the same promise gap).

QMA-hardness results are known for simple lattice models of qubits such as the ZX Hamiltonian $H_{ZX}=\sum _{i}h_{i}Z_{i}+\sum _{i}\Delta _{i}X_{i}+\sum _{i<j}J^{ij}Z_{i}Z_{j}+\sum _{i<j}K^{ij}X_{i}X_{j}$ where $Z,X$ represent the Pauli matrices $\sigma _{z},\sigma _{x}$ . Such models are applicable to universal adiabatic quantum computation.

*k*-local Hamiltonians problems are analogous to classical Constraint Satisfaction Problems. The following table illustrates the analogous gadgets between classical CSPs and Hamiltonians.

| Classical | Quantum | Notes |
|---|---|---|
| Constraint Satisfaction Problem | Hamiltonian |   |
| Variable | Qubit |   |
| Constraint | Hamiltonian Term |   |
| Variable Assignment | Quantum state |   |
| Number of constraints satisfied | Hamiltonian's energy term |   |
| Optimal Solution | Hamiltonian's ground state | The most possible constraints satisfied |

### Other QMA-complete problems

A list of known QMA-complete problems can be found at https://arxiv.org/abs/1212.6312.

**QCMA** (or **MQA**), which stands for Quantum Classical Merlin Arthur (or Merlin Quantum Arthur), is similar to QMA, but the proof has to be a classical string. It is not known whether QMA equals QCMA, although QCMA is clearly contained in QMA.

**QIP(k)**, which stands for Quantum Interactive Polynomial time (k messages), is a generalization of QMA where Merlin and Arthur can interact for k rounds. QMA is QIP(1). QIP(2) is known to be in PSPACE.

**QIP** is QIP(k) where k is allowed to be polynomial in the number of qubits. It is known that QIP(3) = QIP. It is also known that QIP = IP = PSPACE.

## Relationship to other classes

QMA is related to other known complexity classes by the following relations:

${\mathsf {P}}\subseteq {\mathsf {NP}}\subseteq {\mathsf {MA}}\subseteq {\mathsf {QCMA}}\subseteq {\mathsf {QMA}}\subseteq {\mathsf {PP}}\subseteq {\mathsf {PSPACE}}$

The first inclusion follows from the definition of NP. The next two inclusions follow from the fact that the verifier is being made more powerful in each case. QCMA is contained in QMA since the verifier can force the prover to send a classical proof by measuring proofs as soon as they are received. The fact that QMA is contained in PP was shown by Alexei Kitaev and John Watrous. PP is also easily shown to be in PSPACE.

It is unknown if any of these inclusions is unconditionally strict, as it is not even known whether P is strictly contained in PSPACE or P = PSPACE. However, the currently best known upper bounds on QMA are

${\mathsf {QMA}}\subseteq {\mathsf {A_{0}PP}}$

and

${\mathsf {QMA}}\subseteq {\mathsf {P^{QMA[log]}}}$

,

where both ${\mathsf {A_{0}PP}}$ and ${\mathsf {P^{QMA[log]}}}$ are contained in ${\mathsf {PP}}$ . It is unlikely that ${\mathsf {QMA}}$ equals ${\mathsf {P^{QMA[log]}}}$ , as this would imply ${\mathsf {QMA}}={\mathsf {co}}$ - ${\mathsf {QMA}}$ . It is unknown whether ${\mathsf {P^{QMA[log]}}}\subseteq {\mathsf {A_{0}PP}}$ or vice versa.
