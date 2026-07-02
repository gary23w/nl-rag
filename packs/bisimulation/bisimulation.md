---
title: "Bisimulation"
source: https://en.wikipedia.org/wiki/Bisimulation
domain: bisimulation
license: CC-BY-SA-4.0
tags: bisimulation relation, bisimulation equivalence, coinductive proof, labelled transition system
fetched: 2026-07-02
---

# Bisimulation

In theoretical computer science, a **bisimulation** is a binary relation between state transition systems, associating systems that behave in the same way in that one system simulates the other and vice versa.

Intuitively two systems are bisimilar if they, assuming we view them as playing a *game* according to some rules, match each other's moves. In this sense, each of the systems cannot be distinguished from the other by an observer.

## Formal definition

Given a labeled state transition system (*S*, Λ, →), where S is a set of states, $\Lambda$ is a set of labels and → is a set of labelled transitions (i.e., a subset of $S\times \Lambda \times S$ ), a **bisimulation** is a binary relation $R\subseteq S\times S$ , such that both R and its converse $R^{T}$ are simulations. From this follows that the symmetric closure of a bisimulation is a bisimulation, and that each symmetric simulation is a bisimulation. Thus some authors define bisimulation as a symmetric simulation.

Equivalently, R is a **bisimulation** if and only if for every pair of states $(p,q)$ in R and all labels *λ* in $\Lambda$ :

- if $p\mathrel {\overset {\lambda }{\rightarrow }} p'$ , then there is $q\mathrel {\overset {\lambda }{\rightarrow }} q'$ such that $(p',q')\in R$ ;
- if $q\mathrel {\overset {\lambda }{\rightarrow }} q'$ , then there is $p\mathrel {\overset {\lambda }{\rightarrow }} p'$ such that $(p',q')\in R$ .

Given two states p and q in S, p is **bisimilar** to q, written $p\,\sim \,q$ , if and only if there is a bisimulation R such that $(p,q)\in R$ . This means that the bisimilarity relation ∼ is the union of all bisimulations: $(p,q)\in \,\sim \,$ precisely when $(p,q)\in R$ for some bisimulation R.

The set of bisimulations is closed under union; therefore, the bisimilarity relation is itself a bisimulation. Since it is the union of all bisimulations, it is the unique largest bisimulation. Bisimulations are also closed under reflexive, symmetric, and transitive closure; therefore, the largest bisimulation must be reflexive, symmetric, and transitive. From this follows that the largest bisimulation—bisimilarity—is an equivalence relation.

## Alternative definitions

### Relational definition

Bisimulation can be defined in terms of composition of relations as follows.

Given a labelled state transition system $(S,\Lambda ,\rightarrow )$ , a *bisimulation* relation is a binary relation R over S (i.e., *R* ⊆ *S* × *S*) such that $\forall \lambda \in \Lambda$

$R\ ;\ {\overset {\lambda }{\rightarrow }}\quad {\subseteq }\quad {\overset {\lambda }{\rightarrow }}\ ;\ R$ and $R^{-1}\ ;\ {\overset {\lambda }{\rightarrow }}\quad {\subseteq }\quad {\overset {\lambda }{\rightarrow }}\ ;\ R^{-1}$

From the monotonicity and continuity of relation composition, it follows immediately that the set of bisimulations is closed under unions (joins in the poset of relations), and a simple algebraic calculation shows that the relation of bisimilarity—the join of all bisimulations—is an equivalence relation. This definition, and the associated treatment of bisimilarity, can be interpreted in any involutive quantale.

### Fixpoint definition

Bisimilarity can also be defined in order-theoretical fashion, in terms of fixpoint theory, more precisely as the greatest fixed point of a certain function defined below.

Given a labelled state transition system ( S , Λ, →), define $F:{\mathcal {P}}(S\times S)\to {\mathcal {P}}(S\times S)$ to be a function from binary relations over S to binary relations over S , as follows:

Let R be any binary relation over S . $F(R)$ is defined to be the set of all pairs $(p,q)$ in S × S such that:

$\forall \lambda \in \Lambda .\,\forall p'\in S.\,p{\overset {\lambda }{\rightarrow }}p'\,\Rightarrow \,\exists q'\in S.\,q{\overset {\lambda }{\rightarrow }}q'\,{\textrm {and}}\,(p',q')\in R$ and $\forall \lambda \in \Lambda .\,\forall q'\in S.\,q{\overset {\lambda }{\rightarrow }}q'\,\Rightarrow \,\exists p'\in S.\,p{\overset {\lambda }{\rightarrow }}p'\,{\textrm {and}}\,(p',q')\in R$

Bisimilarity is then defined to be the greatest fixed point of F .

### Ehrenfeucht–Fraïssé game definition

Bisimulation can also be thought of in terms of a game between two players: attacker and defender.

"Attacker" goes first and may choose any valid transition, $\lambda$ , from $(p,q)$ . That is, $(p,q){\overset {\lambda }{\rightarrow }}(p',q)$ or $(p,q){\overset {\lambda }{\rightarrow }}(p,q')$

The "Defender" must then attempt to match that transition, $\lambda$ from either $(p',q)$ or $(p,q')$ depending on the attacker's move. I.e., they must find an $\lambda$ such that: $(p',q){\overset {\lambda }{\rightarrow }}(p',q')$ or $(p,q'){\overset {\lambda }{\rightarrow }}(p',q')$

Attacker and defender continue to take alternating turns until:

- The defender is unable to find any valid transitions to match the attacker's move. In this case the attacker wins.
- The game reaches states $(p,q)$ that are both 'dead' (i.e., there are no transitions from either state) In this case the defender wins
- The game goes on forever, in which case the defender wins.
- The game reaches states $(p,q)$ , which have already been visited. This is equivalent to an infinite play and counts as a win for the defender.

By the above definition the system is a bisimulation if and only if there exists a winning strategy for the defender.

### Coalgebraic definition

A bisimulation for state transition systems is a special case of coalgebraic bisimulation for the type of covariant powerset functor. Note that every state transition system $(S,\Lambda ,\rightarrow )$ can be mapped bijectively to a function $\xi _{\rightarrow }$ from S to the powerset of S indexed by $\Lambda$ written as ${\mathcal {P}}(\Lambda \times S)$ , defined by $p\mapsto \{(\lambda ,q)\in \Lambda \times S:p{\overset {\lambda }{\rightarrow }}q\}.$

Let $\pi _{i}\colon S\times S\to S$ be i -th projection, mapping $(p,q)$ to p and q respectively for $i=1,2$ ; and ${\mathcal {P}}(\Lambda \times \pi _{1})$ the forward image of $\pi _{1}$ defined by dropping the third component $P\mapsto \{(\lambda ,p)\in \Lambda \times S:\exists q.(\lambda ,p,q)\in P\}$ where P is a subset of $\Lambda \times S\times S$ . Similarly for ${\mathcal {P}}(\Lambda \times \pi _{2})$ .

Using the above notations, a relation $R\subseteq S\times S$ is a **bisimulation** on a transition system $(S,\Lambda ,\rightarrow )$ if and only if there exists a transition system $\gamma \colon R\to {\mathcal {P}}(\Lambda \times R)$ on the relation R such that the diagram

commutes, i.e. for $i=1,2$ , the equations $\xi _{\rightarrow }\circ \pi _{i}={\mathcal {P}}(\Lambda \times \pi _{i})\circ \gamma$ hold where $\xi _{\rightarrow }$ is the functional representation of $(S,\Lambda ,\rightarrow )$ .

## Variants of bisimulation

In special contexts the notion of bisimulation is sometimes refined by adding additional requirements or constraints. An example is that of stutter bisimulation, in which one transition of one system may be matched with multiple transitions of the other, provided that the intermediate states are equivalent to the starting state ("stutters").

A different variant applies if the state transition system includes a notion of *silent* (or *internal*) action, often denoted with $\tau$ , i.e. actions that are not visible by external observers, then bisimulation can be relaxed to be *weak bisimulation*, in which if two states p and q are bisimilar and there is some number of internal actions leading from p to some state $p'$ then there must exist state $q'$ such that there is some number (possibly zero) of internal actions leading from q to $q'$ . A relation ${\mathcal {R}}$ on processes is a weak bisimulation if the following holds (with ${\mathcal {S}}\in \{{\mathcal {R}},{\mathcal {R}}^{-1}\}$ , and $a,\tau$ being an observable and mute transition respectively):

$\forall p,q.\quad (p,q)\in {\mathcal {S}}\Rightarrow p{\stackrel {\tau }{\rightarrow }}p'\Rightarrow \exists q'.\quad q{\stackrel {\tau ^{\ast }}{\rightarrow }}q'\wedge (p',q')\in {\mathcal {S}}$ $\forall p,q.\quad (p,q)\in {\mathcal {S}}\Rightarrow p{\stackrel {a}{\rightarrow }}p'\Rightarrow \exists q'.\quad q{\stackrel {\tau ^{\ast }a\tau ^{\ast }}{\rightarrow }}q'\wedge (p',q')\in {\mathcal {S}}$

This is closely related to the notion of bisimulation "up to" a relation.

Typically, if the state transition system gives the operational semantics of a programming language, then the precise definition of bisimulation will be specific to the restrictions of the programming language. Therefore, in general, there may be more than one kind of bisimulation (respectively bisimilarity) relationship depending on the context.

## Bisimulation and modal logic

Since Kripke models are a special case of (labelled) state transition systems, bisimulation is also a topic in modal logic. In fact, modal logic is the fragment of first-order logic invariant under bisimulation (van Benthem's theorem).

## Algorithm

Checking that two finite transition systems are bisimilar can be done in polynomial time. The fastest algorithms are quasilinear time using partition refinement through a reduction to the coarsest partition problem.
