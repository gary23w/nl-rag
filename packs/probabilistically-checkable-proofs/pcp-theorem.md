---
title: "PCP theorem"
source: https://en.wikipedia.org/wiki/PCP_theorem
domain: probabilistically-checkable-proofs
license: CC-BY-SA-4.0
tags: probabilistically checkable proof, pcp theorem, proof verification, hardness of approximation
fetched: 2026-07-02
---

# PCP theorem

In computational complexity theory, the **PCP theorem** (also known as the **PCP characterization theorem**) states that every decision problem in the NP complexity class has probabilistically checkable proofs (proofs that can be checked by a randomized algorithm) of constant query complexity and logarithmic randomness complexity (uses a logarithmic number of random bits).

The PCP theorem says that for some universal constant K , for every n , any mathematical proof for a statement of length n can be rewritten as a different proof of length $\operatorname {poly} (n)$ that is formally verifiable with 99% accuracy by a randomized algorithm that inspects only K letters of that proof.

The PCP theorem is the cornerstone of the theory of computational hardness of approximation, which investigates the inherent difficulty in designing efficient approximation algorithms for various optimization problems. It has been described by Ingo Wegener as "the most important result in complexity theory since Cook's theorem" and by Oded Goldreich as "a culmination of a sequence of impressive works […] rich in innovative ideas".

## Formal statement

The PCP theorem states that ${\mathsf {NP}}={\mathsf {PCP}}[O(\log n),O(1)]$ where ${\mathsf {NP}}$ is the complexity class of problems solvable in nondeterministic polynomial time and where ${\mathsf {PCP}}[r(n),q(n)]$ is the class of problems for which a probabilistically checkable proof of a solution can be given, such that the proof can be checked in polynomial time using $r(n)$ bits of randomness and by reading $q(n)$ bits of the proof, correct proofs are always accepted, and incorrect proofs are rejected with probability at least ${\tfrac {1}{2}}$ . The variable n is the length in bits of the description of a problem instance. Note further that the verification algorithm is *non-adaptive*: the choice of bits of the proof to check depend only on the random bits and the description of the problem instance, not the actual bits of the proof.

## PCP and hardness of approximation

An alternative formulation of the PCP theorem states that the maximum fraction of satisfiable constraints of a certain constraint satisfaction problem is NP-hard to approximate within some constant factor.

Formally, for some constants q and $\alpha <1$ , the following promise problem $(L_{\mathrm {yes} },L_{\mathrm {no} })$ is an NP-hard decision problem:

- ${\displaystyle L_{\mathrm {yes} }=\{\Phi$ all constraints in $\Phi$ are simultaneously satisfiable $\}$
- ${\displaystyle L_{\mathrm {no} }=\{\Phi$ every assignment satisfies fewer than an $\alpha$ fraction of $\Phi$ 's constraints $\}$

where $\Phi$ is a constraint satisfaction problem (CSP) over a Boolean alphabet with at most q variables per constraint.

The connection to the class ${\mathsf {PCP}}$ mentioned above can be seen by noticing that checking a constant number of bits q in a proof can be seen as evaluating a constraint in q Boolean variables on those bits of the proof. Since the verification algorithm uses $O(\log n)$ bits of randomness, it can be represented as a CSP as described above with $\operatorname {poly} (n)$ constraints. The first formulation of the PCP theorem then guarantees the promise condition with $\alpha ={\tfrac {1}{2}}$ : if the NP problem's answer is yes, then every constraint (which corresponds to a particular value for the random bits) has a satisfying assignment (an acceptable proof); otherwise, any proof should be rejected with probability at least ${\tfrac {1}{2}}$ , which means any assignment must satisfy fewer than ${\tfrac {1}{2}}$ of the constraints (which means it will be accepted with probability lower than ${\tfrac {1}{2}}$ ). Therefore, an algorithm for the promise problem would be able to solve the underlying NP problem, and hence the promise problem must be NP-hard.

As a consequence of this theorem, it can be shown that the solutions to many natural optimization problems including maximum boolean formula satisfiability, maximum independent set in graphs, and the shortest vector problem for lattices cannot be approximated efficiently unless ${\mathsf {P}}={\mathsf {NP}}$ . This can be done by reducing the problem of approximating a solution to such problems to a promise problem of the above form. These results are sometimes also called PCP theorems because they can be viewed as probabilistically checkable proofs for NP with some additional structure.

## Proof

A proof of a weaker result, ⁠ ${\mathsf {NP}}\subseteq {\mathsf {PCP}}[n^{3},1]$ ⁠ is given in one of the lectures of Dexter Kozen.

## History

The PCP theorem is the culmination of a long line of work on interactive proofs and probabilistically checkable proofs. The first theorem relating standard proofs and probabilistically checkable proofs is the statement that ${\mathsf {NEXP}}\subseteq {\mathsf {PCP}}[\operatorname {poly} (n),\operatorname {poly} (n)]$ , proved by Babai, Fortnow & Lund (1990).

### Origin of the initials

The notation ${\mathsf {PCP}}_{c(n),s(n)}[r(n),q(n)]$ is explained at probabilistically checkable proof. The notation is that of a function that returns a certain complexity class. See the explanation mentioned above.

The name of this theorem (the "PCP theorem") probably comes either from **"PCP"** meaning "probabilistically checkable proof", or from the notation mentioned above (or both).

### First theorem [in 1990]

Subsequently, the methods used in this work were extended by Babai, Lance Fortnow, Levin, and Szegedy in 1991 (Babai et al. 1991), Feige, Goldwasser, Lund, Safra, and Szegedy (1991), and Arora and Safra in 1992 (Arora & Safra 1992) to yield a proof of the PCP theorem by Arora, Lund, Motwani, Sudan, and Szegedy in 1998 (Arora et al. 1998).

The 2001 Gödel Prize was awarded to Sanjeev Arora, Uriel Feige, Shafi Goldwasser, Carsten Lund, László Lovász, Rajeev Motwani, Shmuel Safra, Madhu Sudan, and Mario Szegedy for work on the PCP theorem and its connection to hardness of approximation.

In 2005 Irit Dinur discovered a significantly simpler proof of the PCP theorem, using expander graphs. She received the 2019 Gödel Prize for this.

## Quantum analogs

### Nonlocal games version

A version of the PCP theorem for quantum nonlocal games would state that it is computationally hard to approximate the quantum value of a quantum nonlocal game. In 2012, Thomas Vidick and Tsuyoshi Ito published a result that showed a "strong limitation on the ability of entangled provers to collude in a multiplayer game". This could be a step toward proving the quantum analogue of the PCP theorem, since when the result was reported in the media, professor Dorit Aharonov called it "the quantum analogue of an earlier paper on multiprover interactive proofs" that "basically led to the PCP theorem".

In 2018, Thomas Vidick and Anand Natarajan proved a games variant of quantum PCP theorem under randomized reduction. It states that ${\mathsf {QMA}}\subseteq {\mathsf {MIP}}^{*}[\log n,1,{\tfrac {1}{2}}]$ , where ${\mathsf {MIP}}^{*}[f(n),c,s]$ is a complexity class of multi-prover quantum interactive proofs systems with $f(n)$ -bit classical communications, and the completeness is c and the soundness is s .

### Hamiltonian version

A version of the PCP theorem for quantum local Hamiltonians would state that it is computationally hard to approximate the ground energy of a quantum local Hamiltonian. The work of Natarajan and Vidick also showed that a quantum Hamiltonian version of the PCP theorem, namely the existence of local Hamiltonian problem with constant promise gap $c-s$ which are QMA-hard, implies a quantum nonlocal games version of the PCP theorem.

The NLTS conjecture was an unresolved obstacle and precursor to a quantum Hamiltonian analog of the PCP theorem. The conjecture was proven in 2022 by Anurag Anshu, Nikolas Breuckmann, and Chinmay Nirkhe using a construction of a Hamiltonian based on quantum CSS codes. However, the ground states of such Hamiltonians are given explicitly by the code states of the corresponding CSS code, and thus are not computationally hard enough for a general proof of a quantum PCP theorem.
