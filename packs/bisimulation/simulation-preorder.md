---
title: "Simulation (computer science)"
source: https://en.wikipedia.org/wiki/Simulation_preorder
domain: bisimulation
license: CC-BY-SA-4.0
tags: bisimulation relation, bisimulation equivalence, coinductive proof, labelled transition system
fetched: 2026-07-02
---

# Simulation (computer science)

(Redirected from

Simulation preorder

)

In theoretical computer science, a **simulation** is a relation between state transition systems associating systems that behave in the same way in the sense that one system *simulates* the other.

Intuitively, a system simulates another system if it can match all of its moves.

The basic definition relates states within one transition system, but this is easily adapted to relate two separate transition systems by building a system consisting of the disjoint union of the corresponding components.

## Formal definition

Given a labelled state transition system ( S , $\Lambda$ , →), where S is a set of states, $\Lambda$ is a set of labels and → is a set of labelled transitions (i.e., a subset of $S\times \Lambda \times S$ ), a relation $R\subseteq S\times S$ is a **simulation** if and only if for every pair of states $(p,q)$ in R and all labels λ in $\Lambda$ :

if

$p{\overset {\lambda }{\rightarrow }}p'$

, then there is

$q{\overset {\lambda }{\rightarrow }}q'$

such that

$(p',q')\in R$

Equivalently, in terms of relational composition:

$R^{-1}\,;\,{\overset {\lambda }{\rightarrow }}\quad {\subseteq }\quad {\overset {\lambda }{\rightarrow }}\,;\,R^{-1}$

Given two states p and q in S , p can be **simulated** by q , written $p\,\leq \,q$ , if and only if there is a simulation R such that $(p,q)\in R$ . The relation $\leq$ is called the **simulation preorder**, and it is the union of all simulations: $(p,q)\in \,\leq \,$ precisely when $(p,q)\in R$ for some simulation R .

The set of simulations is closed under union; therefore, the simulation preorder is itself a simulation. Since it is the union of all simulations, it is the unique largest simulation. Simulations are also closed under reflexive and transitive closure; therefore, the largest simulation must be reflexive and transitive. From this follows that the largest simulation—the simulation preorder—is indeed a preorder relation. Note that there can be more than one relation that is both a simulation and a preorder; the term *simulation preorder* refers to the largest one of them (which is a superset of all the others).

Two states p and q are said to be **similar**, written $p\leq \geq q$ , if and only if p can be simulated by q and q can be simulated by p . Similarity is thus the maximal symmetric subset of the simulation preorder, which means it is reflexive, symmetric, and transitive; hence an equivalence relation. However, it is not necessarily a simulation, and precisely in those cases when it is not a simulation, it is strictly coarser than bisimilarity (meaning it is a superset of bisimilarity). To witness, consider a similarity that *is* a simulation. Since it is symmetric, it is a *bisimulation*. It must then be a *subset* of bisimilarity, which is the union of all bisimulations. Yet it is easy to see that similarity is always a *superset* of bisimilarity. From this follows that if similarity is a simulation, it equals bisimilarity. And if it equals bisimilarity, it is naturally a simulation (since bisimilarity is a simulation). Therefore, similarity is a simulation if and only if it equals bisimilarity. If it does not, it must be its strict superset; hence a strictly coarser equivalence relation.

## Similarity of separate transition systems

When comparing two different transition systems (S', Λ', →') and (S", Λ", →"), the basic notions of simulation and similarity can be used by forming the disjoint composition of the two machines, (S, Λ, →) with S = S' ∐ S", Λ = Λ' ∪ Λ" and → = →' ∪ →", where ∐ is the disjoint union operator between sets.
