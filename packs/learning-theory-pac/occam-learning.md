---
title: "Occam learning"
source: https://en.wikipedia.org/wiki/Occam_learning
domain: learning-theory-pac
license: CC-BY-SA-4.0
tags: probably approximately correct, sample complexity, pac learnable, concept class
fetched: 2026-07-02
---

# Occam learning

In computational learning theory, **Occam learning** is a model of algorithmic learning where the objective of the learner is to output a succinct representation of received training data. This is closely related to probably approximately correct (PAC) learning, where the learner is evaluated on its predictive power of a test set.

Occam learnability implies PAC learning, and for a wide variety of concept classes, the converse is also true: PAC learnability implies Occam learnability.

## Introduction

Occam Learning is named after Occam's razor, which is a principle stating that, given all other things being equal, a shorter explanation for observed data should be favored over a lengthier explanation. The theory of Occam learning is a formal and mathematical justification for this principle. It was first shown by Blumer, et al. that Occam learning implies PAC learning, which is the standard model of learning in computational learning theory. In other words, *parsimony* (of the output hypothesis) implies *predictive power*.

## Definition of Occam learning

The succinctness of a concept c in concept class ${\mathcal {C}}$ can be expressed by the length $size(c)$ of the shortest bit string that can represent c in ${\mathcal {C}}$ . Occam learning connects the succinctness of a learning algorithm's output to its predictive power on unseen data.

Let ${\mathcal {C}}$ and ${\mathcal {H}}$ be concept classes containing target concepts and hypotheses respectively. Then, for constants $\alpha \geq 0$ and $0\leq \beta <1$ , a learning algorithm L is an **$(\alpha ,\beta )$ -Occam algorithm** for ${\mathcal {C}}$ using ${\mathcal {H}}$ iff, given a set $S=\{x_{1},\dots ,x_{m}\}$ of m samples labeled according to a concept $c\in {\mathcal {C}}$ , L outputs a hypothesis $h\in {\mathcal {H}}$ such that

- h is consistent with c on S (that is, $h(x)=c(x),\forall x\in S$ ), and
- $size(h)\leq (n\cdot size(c))^{\alpha }m^{\beta }$

where n is the maximum length of any sample $x\in S$ . An Occam algorithm is called *efficient* if it runs in time polynomial in n , m , and $size(c).$ We say a concept class ${\mathcal {C}}$ is *Occam learnable* with respect to a hypothesis class ${\mathcal {H}}$ if there exists an efficient Occam algorithm for ${\mathcal {C}}$ using ${\mathcal {H}}.$

## The relation between Occam and PAC learning

Occam learnability implies PAC learnability, as the following theorem of Blumer, et al. shows:

### Theorem (*Occam learning implies PAC learning*)

> Let L be an efficient **$(\alpha ,\beta )$**-Occam algorithm for ${\mathcal {C}}$ using ${\mathcal {H}}$ . Then there exists a constant $a>0$ such that for any $0<\epsilon ,\delta <1$ , for any distribution ${\mathcal {D}}$ , given $m\geq a\left({\frac {1}{\epsilon }}\log {\frac {1}{\delta }}+\left({\frac {(n\cdot size(c))^{\alpha }}{\epsilon }}\right)^{\frac {1}{1-\beta }}\right)$ samples drawn from ${\mathcal {D}}$ and labelled according to a concept $c\in {\mathcal {C}}$ of length n bits each, the algorithm L will output a hypothesis $h\in {\mathcal {H}}$ such that $error(h)\leq \epsilon$ with probability at least $1-\delta$ .

Here, $error(h)$ is with respect to the concept c and distribution ${\mathcal {D}}$ . This implies that the algorithm L is also a PAC learner for the concept class ${\mathcal {C}}$ using hypothesis class ${\mathcal {H}}$ . A slightly more general formulation is as follows:

### Theorem (*Occam learning implies PAC learning, cardinality version*)

> Let $0<\epsilon ,\delta <1$ . Let L be an algorithm such that, given m samples drawn from a fixed but unknown distribution ${\mathcal {D}}$ and labeled according to a concept $c\in {\mathcal {C}}$ of length n bits each, outputs a hypothesis $h\in {\mathcal {H}}_{n,m}$ that is consistent with the labeled samples. Then, there exists a constant b such that if $\log |{\mathcal {H}}_{n,m}|\leq b\epsilon m-\log {\frac {1}{\delta }}$ , then L is guaranteed to output a hypothesis $h\in {\mathcal {H}}_{n,m}$ such that $error(h)\leq \epsilon$ with probability at least $1-\delta$ .

While the above theorems show that Occam learning is sufficient for PAC learning, it doesn't say anything about *necessity.* Board and Pitt show that, for a wide variety of concept classes, Occam learning is in fact necessary for PAC learning. They proved that for any concept class that is *polynomially closed under exception lists,* PAC learnability implies the existence of an Occam algorithm for that concept class. Concept classes that are polynomially closed under exception lists include Boolean formulas, circuits, deterministic finite automata, decision-lists, decision-trees, and other geometrically defined concept classes.

A concept class ${\mathcal {C}}$ is polynomially closed under exception lists if there exists a polynomial-time algorithm A such that, when given the representation of a concept $c\in {\mathcal {C}}$ and a finite list E of *exceptions*, outputs a representation of a concept $c'\in {\mathcal {C}}$ such that the concepts c and $c'$ agree except on the set E .

## Proof that Occam learning implies PAC learning

We first prove the Cardinality version. Call a hypothesis $h\in {\mathcal {H}}$ *bad* if $error(h)\geq \epsilon$ , where again $error(h)$ is with respect to the true concept c and the underlying distribution ${\mathcal {D}}$ . The probability that a set of samples S is consistent with h is at most $(1-\epsilon )^{m}$ , by the independence of the samples. By the union bound, the probability that there exists a bad hypothesis in ${\mathcal {H}}_{n,m}$ is at most $|{\mathcal {H}}_{n,m}|(1-\epsilon )^{m}$ , which is less than $\delta$ if $\log |{\mathcal {H}}_{n,m}|\leq O(\epsilon m)-\log {\frac {1}{\delta }}$ . This concludes the proof of the second theorem above.

Using the second theorem, we can prove the first theorem. Since we have a $(\alpha ,\beta )$ -Occam algorithm, this means that any hypothesis output by L can be represented by at most $(n\cdot size(c))^{\alpha }m^{\beta }$ bits, and thus $\log |{\mathcal {H}}_{n,m}|\leq (n\cdot size(c))^{\alpha }m^{\beta }$ . This is less than $O(\epsilon m)-\log {\frac {1}{\delta }}$ if we set $m\geq a\left({\frac {1}{\epsilon }}\log {\frac {1}{\delta }}+\left({\frac {(n\cdot size(c))^{\alpha })}{\epsilon }}\right)^{\frac {1}{1-\beta }}\right)$ for some constant $a>0$ . Thus, by the Cardinality version Theorem, L will output a consistent hypothesis h with probability at least $1-\delta$ . This concludes the proof of the first theorem above.

## Improving sample complexity for common problems

Though Occam and PAC learnability are equivalent, the Occam framework can be used to produce tighter bounds on the sample complexity of classical problems including conjunctions, conjunctions with few relevant variables, and decision lists.

## Extensions

Occam algorithms have also been shown to be successful for PAC learning in the presence of errors, probabilistic concepts, function learning and Markovian non-independent examples.
