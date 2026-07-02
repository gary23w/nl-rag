---
title: "Proof complexity"
source: https://en.wikipedia.org/wiki/Proof_complexity
domain: proof-complexity
license: CC-BY-SA-4.0
tags: proof complexity, resolution refutation, propositional proof system, frege system
fetched: 2026-07-02
---

# Proof complexity

In logic and theoretical computer science, and specifically proof theory and computational complexity theory, **proof complexity** is the field aiming to understand and analyse the computational resources that are required to prove or refute statements. Research in proof complexity is predominantly concerned with proving proof-length lower and upper bounds in various propositional proof systems. For example, among the major challenges of proof complexity is showing that the Frege system, the usual propositional calculus, does not admit polynomial-size proofs of all tautologies. Here the size of the proof is simply the number of symbols in it, and a proof is said to be of polynomial size if it is polynomial in the size of the tautology it proves.

Systematic study of proof complexity began with the work of Stephen Cook and Robert Reckhow (1979), who provided the basic definition of a propositional proof system from the perspective of computational complexity. Specifically, Cook and Reckhow observed that proving proof size lower bounds on stronger and stronger propositional proof systems can be viewed as a step towards separating NP from co-NP (and thus P from NP), since the existence of a propositional proof system that admits polynomial size proofs for all tautologies is equivalent to NP = co-NP.

Contemporary proof complexity research draws ideas and methods from many areas in computational complexity, algorithms and mathematics. Since many important algorithms and algorithmic techniques can be cast as proof search algorithms for certain proof systems, proving lower bounds on proof sizes in these systems implies run-time lower bounds on the corresponding algorithms. This connects proof complexity to more applied areas such as SAT solving.

Mathematical logic can also serve as a framework to study propositional proof sizes. First-order theories and, in particular, weak fragments of Peano arithmetic, which come under the name of bounded arithmetic, serve as uniform versions of propositional proof systems and provide further background for interpreting short propositional proofs in terms of various levels of feasible reasoning.

## Main concepts

### Conventions

By default, proof theory discussed proof systems for classical propositional logic, using the **language** of propositional logic with the connectives $\land ,\lor ,\neg ,\to$ , and countably many propositional variables $\{p_{i}:i\in 2^{*}\}$ . Here, $2^{*}$ is the set of finite binary strings.

A **proof system** is denoted with capital letters: $P,Q,R,\dots$ . A **proof** is denoted with lowercase letters $x,y,z,\dots$ .

A **formula** is denoted with lower Greek letters: $\phi ,\psi ,\sigma ,\dots$ . The **length** of a formula $\phi$ is $|\phi |$ . Similarly, the length of a proof x is $|x|$ .

TAUT is a formal language consisting of the tautological formulas of propositional logic.

Big-O and big-Omega notation are used in the same way as in computational complexity theory.

### Proof systems

A proof system is an algorithm P that takes two inputs: a formula $\phi$ , and a purported proof x . The proof system must satisfy:

- $P(\phi ,x)$ runs in time ${\mathsf {poly}}(|\phi |,|x|)$ .
- $\phi \in {\mathsf {TAUT}}$ if and only if there exists some x , such that $P(\phi ,x)$ accepts.

Examples of propositional proof systems include sequent calculus, resolution, cutting planes and Frege systems. Strong mathematical theories such as ZFC induce propositional proof systems as well: a proof of a tautology $\tau$ in a propositional interpretation of ZFC is a ZFC-proof of a formalized statement ' $\tau$ is a tautology'.

A proof system can be thought of as a nondeterministic polynomial-time algorithm for proving non-satisfiability. That is, given a formula $\phi$ , $\phi$ is unsatisfiable if and only if there exists some x , such that $P(\neg \phi ,x)$ accepts. This shows its close relationship with the co-NP class.

### Complexity

Ordinary proof theory does not care about what formulas a certain proof system *can and cannot* prove. Proof complexity is not satisfied with what *can* be done, but *how efficiently* it can be done, i.e. the computational complexity of the proof system. In order to measure efficiency, what efficiency is for a proof system must be defined.

In ordinary complexity theory, efficiency can be measured by how many steps are required (time complexity), how much working space is required (space complexity), size of a Boolean circuit needed to implement a boolean function (circuit complexity), etc. In proof complexity theory, there are also more than one way to measure of efficiency.

The **size complexity** of a proof system denotes the minimal size of proofs possible in the system for a given tautology. In detail, a proof system has (upper bound) size complexity $O(F(n))$ iff given any tautology $\phi$ of length n , there is a proof of $\phi$ in this proof system that uses $\lesssim F(n)$ steps. It has (lower bound) size complexity $\Omega (F(n))$ iff given any length n , there exists a tautology $\phi$ of length n , such that any proof of $\phi$ in the proof system needs $\gtrsim F(n)$ steps.

The **space complexity** of a proof system denotes the memory usage during a proof. A common way to measure "memory usage" is **clause complexity**: the maximum number of clauses that can appear simultaneously during a resolution proof. Other ways to measure space complexity include:

- The number of symbols of a proof.
- The number of lines of a proof.
- The maximal complexity of formulas that appears in a proof. The complexity of a formula may be its length, or its number of variables, or its number of quantifiers, etc.
- The depth of a proof-tree (in the case of natural deduction or sequent calculus).
- The memory complexity of a proof. One can imagine a proof system as having a memory bank, such that at any point in the proof, only formulas in the bank, or axioms, may be used. A formula may be removed from the memory bank, but if that formula needs to be used again, it must be re-proven. Then, the memory complexity of the proof is the minimal number of memory locations necessary for the proof to go through.

The **search complexity** of a proof system denotes the computational complexity of a prover, that is, an algorithm for finding a proof of a tautology within a proof system. A proof system with a polynomial-time prover is **automatable**.

## Proof size complexity

### p-boundedness

A proof system P is polynomially bounded (**p-bounded**) iff for any $\phi$ , if there exists some x such that $P(\phi ,x)$ is true, then there exists some x such that $P(\phi ,x)$ is true, and $|x|={\mathsf {poly}}(|\phi |)$ . In other words, anything that the system can prove at all, has a polynomially-short proof.

Most nontrivial proof systems are believed to be not p-bounded. To acquire intuition about why this is the case, one consider the following examples.

#### Graph coloring

Given a graph $G=(V,E)$ , if there exists a 3-coloring, then this can be proven by simply giving the coloring. Thus, the proof of 3-colorability has length $|V|$ . It can be checked in polynomial time. In contrast, if there does *not* exist a 3-coloring, then there is no obvious way to prove it succinctly. The naive way to prove it is to explicitly enumerate all $3^{|V|}$ possible 3-colorings, and showing that in each case, there are two vertices of the same color sharing an edge. However, such a proof is exponentially large compared to the input size.

The Hajós construction is a sound and complete proof system for graph non-3-colorability: A graph is non-3-colorable if and only if it has a Hajós 4-construction. However, such a construction may require superpolynomially steps.

#### Polynomial

Given a system of polynomials $f_{1}(x_{1},\dots ,x_{n}),\dots ,f_{m}(x_{1},\dots ,x_{n})$ in a finite field $\mathbb {F}$ , if there exists a root, then this can be proven by simply giving the values for the variables $x_{1},\dots ,x_{n}$ . The proof size is linear in input size. It can be checked in polynomial time.

However, if there is no root, then there is no obvious way to prove it succinctly. The naive way to prove it is to explicitly enumerate all $|\mathbb {F} |^{n}$ possible values. By Hilbert's Nullstellensatz, there is a sound and complete proof system for non-solvability: There exists some polynomials $g_{1},\dots ,g_{m}$ such that $\sum _{i=1}^{m}g_{i}f_{i}=1$ , if and only if the polynomial system is non-solvable. However, the polynomials $g_{1},\dots ,g_{m}$ may contain superpolynomially many terms.

#### Tautology

Given a formula $\phi$ in classical propositional logic with propositional variables $p_{1},\dots ,p_{n}$ , if it is not a tautology, then this can be proven by simply giving the truth-values for the propositional variables $p_{1},\dots ,p_{n}$ , such that $\phi$ evaluates to False. The proof size is linear in input size. However, if it is a tautology, then there is no obvious way to prove it succinctly. The naive way to prove it is to explicitly enumerate the truth table, which has $2^{n}$ rows.

There are many sound and complete proof systems for proving tautologies of classical propositional logic, but there is no guarantee that any system can prove all tautologies with proof size ${\mathsf {poly}}(|\phi |)$ .

### Main results

Unsolved problem in computer science

Does there exist a p-bounded proof system for classical propositional tautologies?

More unsolved problems in computer science

Because $\phi$ is not a tautology if and only if $\neg \phi$ is satisfiable, ${\mathsf {TAUT}}$ is co-NP-complete. Thus, if there exists a proof system for ${\mathsf {TAUT}}$ that is p-bounded, then NP = co-NP. Conversely, if NP = co-NP, then ${\mathsf {TAUT}}$ , being co-NP, would also be NP, and thus there is a p-bounded proof system for proving tautologies. This was first proven by Cook and Reckhow (1979). This results in an equivalent formulation of the NP = coNP problem:

> Does there exist a p-bounded proof system for classical propositional tautologies?

## Proof system strength

Proof complexity compares the strength of proof systems using the notion of *efficient simulation*. Efficiency is the operative concept here, since proof complexity theory studies not merely whether something can be proven, but in the efficiency of the proof.

### Definitions

Given two proof systems $P,Q$ , P **simulates** Q , written as $P\leq Q$ , if and only if there is an algorithm that:

- given as input, a *Q*-proof of a tautology, outputs a *P*-proof of the same tautology,
- and the size of the *P*-proof is polynomial in the size of the *Q*-proof.

We say that P **p-simulates** Q , written as $P\leq _{p}Q$ if and only if there is an algorithm that:

- given as input, a *Q*-proof of a tautology, outputs a *P*-proof of the same tautology,
- and runs in polynomial time polynomial in the size of the *Q*-proof.

Since a polynomial-time algorithm can only produce a polynomial-size output, p-simulation implies simulation. The converse may not hold, i.e. two proof systems $P,Q$ may exist such that P simulates Q , but P does not p-simulate Q .

Both simulation and p-simulation relations are reflexive and transitive, thus they are preorders, and induces equivalence relations. If $P,Q$ (p-)simulate each other, then they are **(p-)equivalent**. A proof system is **(p-)optimal** if it (p-)simulates all other proof systems.

### Results

Any nonempty set in NP has an optimal proof system. No set outside of NP is known to have an optimal proof system. Any coNE-hard sets and even all coNQP-hard sets is known to have no optimal proof systems.

Sequent calculus is p-equivalent to (every) Frege system.

Every propositional proof system *P* can be simulated by Extended Frege extended with axioms postulating soundness of *P*.

Unsolved problem in computer science

Does there exist a p-optimal or optimal propositional proof system?

More unsolved problems in computer science

An optimal or p-optimal propositional proof system would be ideal in a sense, since it would produce the shortest (up to a polynomial factor) possible proofs for all tautologies. Unfortunately, this question is open.

It is known that:

- If E = NE, then there exists of an optimal proof system.
- If NE = co-NE, then there exists of an optimal proof system.

It has been proven that many weak proof systems cannot simulate certain stronger systems (see below). However, the question remains open if the notion of simulation is relaxed. For example, it is open whether Resolution *effectively polynomially simulates* Extended Frege.

## Automatability

The search complexity of proof systems asks:

> Given a proof system, is there an efficient prover of tautologies in this system?

A proof system *P* is **automatable** if there is an algorithm T , called the **prover**, such that:

- If $\tau$ is a tautology, then $P(\tau ,T(\tau ))$ is true. That is, the algorithm outputs a *P*-proof of $\tau$ . Note that there is no requirement for what the algorithm should do when $\tau$ is not a tautology.
- $T(\tau )$ is computable in time ${\mathsf {poly}}(|\tau |,|x|)$ , where x is the shortest *P*-proof of $\tau$ .

The second requirement incorporates the proviso of "the shortest *P*-proof of $\tau$ ", so that even if P is not polynomially bounded, it can still be automatable. That is, there may be tautologies such that the proof system *P* is forced to prove with proofs that are growing super-polynomially. Nevertheless, the prover does the best it could out of a bad situation.

More generally, a proof system P is **weakly automatable** if there is another proof system *R*, and a prover T , such that:

- If $\tau$ is a tautology, then $R(\tau ,T(\tau ))$ is true. That is, the algorithm outputs an *R*-proof of $\tau$ .
- $T(\tau )$ is computable in time ${\mathsf {poly}}(|\tau |,|x|)$ , where x is the shortest *P*-proof of $\tau$ .

### Results

Many proof systems of interest are believed to be non-automatable. However, currently only conditional negative results are known.

- Krajíček and Pudlák (1998) proved that Extended Frege is not weakly automatable unless RSA is not secure against P/poly.
- Bonet, Pitassi and Raz (2000) proved that the $TC^{0}$ -Frege system is not weakly automatable unless the Diffie–Hellman scheme is not secure against P/poly. This was extended by Bonet, Domingo, Gavaldá, Maciel and Pitassi (2004) who proved that constant-depth Frege systems of depth at least 2 are not weakly automatable unless the Diffie–Hellman scheme is not secure against nonuniform adversaries working in subexponential time.
- Alekhnovich and Razborov (2008) proved that tree-like Resolution and Resolution are not automatable unless FPT=W[P]. This was extended by Galesi and Lauria (2010) who proved that Nullstellensatz and Polynomial Calculus are not automatable unless the fixed-parameter hierarchy collapses. Mertz, Pitassi and Wei (2019) proved that tree-like Resolution and Resolution are not automatable even in certain quasi-polynomial time assuming the exponential time hypothesis.
- Atserias and Müller (2019) proved that Resolution is not automatable unless P=NP. This was extended by de Rezende, Göös, Nordström, Pitassi, Robere and Sokolov (2020) to NP-hardness of automating Nullstellensatz and Polynomial Calculus; by Göös, Koroth, Mertz and Pitassi (2020) to NP-hardness of automating Cutting Planes; and by Garlík (2020) to NP-hardness of automating *k*-DNF Resolution.

It is not known if the weak automatability of Resolution would break any standard complexity-theoretic hardness assumptions.

On the positive side,

- Beame and Pitassi (1996) showed that tree-like Resolution is automatable in quasi-polynomial time and Resolution is automatable on formulas of small width in weakly subexponential time.

## Bounded arithmetic

Propositional proof systems can be interpreted as nonuniform equivalents of theories of higher order. The equivalence is most often studied in the context of theories of bounded arithmetic. For example, the Extended Frege system corresponds to Cook's theory $\mathrm {PV} _{1}$ formalizing polynomial-time reasoning and the Frege system corresponds to the theory $\mathrm {VNC} ^{1}$ formalizing ${\mathsf {NC}}^{1}$ reasoning.

The correspondence was introduced by Stephen Cook (1975), who showed that coNP theorems, formally $\Pi _{1}^{b}$ formulas, of the theory $\mathrm {PV} _{1}$ translate to sequences of tautologies with polynomial-size proofs in Extended Frege. Moreover, Extended Frege is the weakest such system: if another proof system *P* has this property, then *P* simulates Extended Frege.

An alternative translation between second-order statements and propositional formulas given by Jeff Paris and Alex Wilkie (1985) has been more practical for capturing subsystems of Extended Frege such as Frege or constant-depth Frege.

While the above-mentioned correspondence says that proofs in a theory translate to sequences of short proofs in the corresponding proof system, a form of the opposite implication holds as well. It is possible to derive lower bounds on size of proofs in a proof system *P* by constructing suitable models of a theory *T* corresponding to the system *P*. This allows to prove complexity lower bounds via model-theoretic constructions, an approach known as Ajtai's method.

## SAT solvers

Propositional proof systems can be interpreted as nondeterministic algorithms for recognizing tautologies. Proving a superpolynomial lower bound on a proof system *P* thus rules out the existence of a polynomial-time algorithm for SAT based on *P*. For example, runs of the DPLL algorithm on unsatisfiable instances correspond to tree-like Resolution refutations. Therefore, exponential lower bounds for tree-like Resolution (see below) rule out the existence of efficient DPLL algorithms for SAT. Similarly, exponential Resolution lower bounds imply that SAT solvers based on Resolution, such as CDCL algorithms cannot solve SAT efficiently (in worst-case).

## Lower bounds

Proving lower bounds on lengths of propositional proofs is generally very difficult. Nevertheless, several methods for proving lower bounds for weak proof systems have been discovered.

- Haken (1985) proved an exponential lower bound for Resolution and the pigeonhole principle.
- Ajtai (1988) proved a superpolynomial lower bound for the constant-depth Frege system and the pigeonhole principle. This was strengthened to an exponential lower bound by Krajíček, Pudlák and Woods and by Pitassi, Beame and Impagliazzo. Ajtai's lower bound uses the method of random restrictions, which was used also to derive AC0 lower bounds in circuit complexity.
- Krajíček (1994) formulated a method of feasible interpolation and later used it to derive new lower bounds for Resolution and other proof systems.
- Pudlák (1997) proved exponential lower bounds for cutting planes via feasible interpolation.
- Ben-Sasson and Wigderson (1999) provided a proof method reducing lower bounds on size of Resolution refutations to lower bounds on width of Resolution refutations, which captured many generalizations of Haken's lower bound.

It is a long-standing open problem to derive a nontrivial lower bound for the Frege system.

## Feasible interpolation

Consider a tautology of the form $A(x,y)\rightarrow B(y,z)$ . The tautology is true for every choice of y , and after fixing y the evaluation of A and B are independent because they are defined on disjoint sets of variables. This means that it is possible to define an *interpolant* circuit $C(y)$ , such that both $A(x,y)\rightarrow C(y)$ and $C(y)\rightarrow B(y,z)$ hold. The interpolant circuit decides either if $A(x,y)$ is false or if $B(y,z)$ is true, by only considering y . The nature of the interpolant circuit can be arbitrary. Nevertheless, it is possible to use a proof of the initial tautology $A(x,y)\rightarrow B(y,z)$ as a hint on how to construct C . A proof systems *P* is said to have *feasible interpolation* if the interpolant $C(y)$ is efficiently computable from any proof of the tautology $A(x,y)\rightarrow B(y,z)$ in *P*. The efficiency is measured with respect to the length of the proof: it is easier to compute interpolants for longer proofs, so this property seems to be anti-monotone in the strength of the proof system.

The following three statements cannot be simultaneously true: (a) $A(x,y)\rightarrow B(y,z)$ has a short proof in a some proof system; (b) such proof system has feasible interpolation; (c) the interpolant circuit solves a computationally hard problem. It is clear that (a) and (b) imply that there is a small interpolant circuit, which is in contradiction with (c). Such relation allows the conversion of proof length upper bounds into lower bounds on computations, and dually to turn efficient interpolation algorithms into lower bounds on proof length.

Some proof systems such as Resolution and Cutting Planes admit feasible interpolation or its variants.

Feasible interpolation can be seen as a weak form of automatability. In fact, for many proof systems, such as Extended Frege, feasible interpolation is equivalent to weak automatability. Specifically, many proof systems *P* are able to prove their own soundness, which is a tautology $\mathrm {Ref} _{P}(\pi ,\phi ,x)$ stating that `if $\pi$ is a *P*-proof of a formula $\phi (x)$ then $\phi (x)$ holds'. Here, $\pi ,\phi ,x$ are encoded by free variables. Moreover, it is possible to generate *P*-proofs of $\mathrm {Ref} _{P}(\pi ,\phi ,x)$ in polynomial-time given the length of $\pi$ and $\phi$ . Therefore, an efficient interpolant resulting from short *P*-proofs of soundness of *P* would decide whether a given formula $\phi$ admits a short *P*-proof $\pi$ . Such an interpolant can be used to define a proof system *R* witnessing that *P* is weakly automatable. On the other hand, weak automatability of a proof system *P* implies that *P* admits feasible interpolation. However, if a proof system *P* does not prove efficiently its own soundness, then it might not be weakly automatable even if it admits feasible interpolation.

Many non-automatability results provide evidence against feasible interpolation in the respective systems.

- Krajíček and Pudlák (1998) proved that Extended Frege does not admit feasible interpolation unless RSA is not secure against P/poly.
- Bonet, Pitassi and Raz (2000) proved that the $TC^{0}$ -Frege system does not admit feasible interpolation unless the Diffie–Helman scheme is not secure against P/poly.
- Bonet, Domingo, Gavaldá, Maciel, Pitassi (2004) proved that constant-depth Frege systems of do not admit feasible interpolation unless the Diffie–Helman scheme is not secure against nonuniform adversaries working in subexponential time.

## Non-classical logics

Many of these questions can be asked about propositional non-classical logics too, such as intuitionistic, modal, and non-monotonic logics.

Hrubeš (2007–2009) proved exponential lower bounds on size of proofs in the Extended Frege system in some modal logics and in intuitionistic logic using a version of monotone feasible interpolation.
