---
title: "Turing degree"
source: https://en.wikipedia.org/wiki/Turing_degree
domain: recursion-theory
license: CC-BY-SA-4.0
tags: computability theory, turing degree, halting problem, arithmetical hierarchy
fetched: 2026-07-02
---

# Turing degree

In computer science and mathematical logic the **Turing degree** (named after Alan Turing) or **degree of unsolvability** of a set of natural numbers measures the level of algorithmic unsolvability of the set.

## Overview

The concept of Turing degree is fundamental in computability theory, where sets of natural numbers are often regarded as decision problems. The Turing degree of a set is a measure of how difficult it is to solve the decision problem associated with the set, that is, to determine whether an arbitrary number is in the given set.

Two sets are **Turing equivalent** if they have the same level of unsolvability; each Turing degree is a collection of Turing equivalent sets, so that two sets are in different Turing degrees exactly when they are not Turing equivalent. Furthermore, the Turing degrees are partially ordered, so that if the Turing degree of a set *X* is less than the Turing degree of a set *Y*, then any (possibly noncomputable) procedure that correctly decides whether numbers are in *Y* can be effectively converted to a procedure that correctly decides whether numbers are in *X*. It is in this sense that the Turing degree of a set corresponds to its level of algorithmic unsolvability.

The Turing degrees were introduced by Post (1944) and many fundamental results were established by Kleene & Post (1954). The Turing degrees have been an area of intense research since then. Many proofs in the area make use of a proof technique known as the **priority method**.

## Turing equivalence

For the rest of this article, the word *set* will refer to a set of natural numbers. A set *X* is said to be **Turing reducible** to a set *Y* if there is an oracle Turing machine that decides membership in *X* when given an oracle for membership in *Y*. The notation *X* ≤T *Y* indicates that *X* is Turing reducible to *Y*.

Two sets *X* and *Y* are defined to be **Turing equivalent** if *X* is Turing reducible to *Y* and *Y* is Turing reducible to *X*. The notation *X* ≡T *Y* indicates that *X* and *Y* are Turing equivalent. The relation ≡T can be seen to be an equivalence relation, which means that for all sets *X*, *Y*, and *Z*:

- *X* ≡T *X*
- *X* ≡T *Y* implies *Y* ≡T *X*
- If *X* ≡T *Y* and *Y* ≡T *Z* then *X* ≡T *Z*.

A **Turing degree** is an equivalence class of the relation ≡T. The notation [*X*] denotes the equivalence class containing a set *X*. The entire collection of Turing degrees is denoted ${\mathcal {D}}$ .

The Turing degrees have a partial order ≤ defined so that [*X*] ≤ [*Y*] if and only if *X* ≤T *Y*. There is a unique Turing degree containing all the computable sets, and this degree is less than every other degree. It is denoted **0** (zero) because it is the least element of the poset ${\mathcal {D}}$ . (It is common to use boldface notation for Turing degrees, in order to distinguish them from sets. When no confusion can occur, such as with [*X*], the boldface is not necessary.)

For any sets *X* and *Y*, the set *X* **join** *Y*, written *X* ⊕ *Y*, is defined to be the union of the sets {2*n* : *n* ∈ *X*} and {2*m*+1 : *m* ∈ *Y*}. The Turing degree of *X* ⊕ *Y* is the least upper bound of the degrees of *X* and *Y*. Thus ${\mathcal {D}}$ is a join-semilattice. The least upper bound of degrees **a** and **b** is denoted **a** ∪ **b**. It is known that ${\mathcal {D}}$ is not a lattice, as there are pairs of degrees with no greatest lower bound.

For any set *X* the notation *X*′ denotes the set of indices of oracle machines that halt (when given their index as input) when using *X* as an oracle. The set *X*′ is called the **Turing jump** of *X*. The Turing jump of a degree [*X*] is defined to be the degree [*X*′]; this is a valid definition because *X*′ ≡T *Y*′ whenever *X* ≡T *Y*. A key example is **0**′, the degree of the halting problem.

## Basic properties of the Turing degrees

- Every Turing degree is countably infinite, that is, it contains exactly $\aleph _{0}$ sets.
- There are $2^{\aleph _{0}}$ distinct Turing degrees.
- For each degree **a** the strict inequality **a** < **a**′ holds.
- For each degree **a**, the set of degrees below **a** is countable. The set of degrees greater than **a** has size $2^{\aleph _{0}}$ .

## Structure of the Turing degrees

A great deal of research has been conducted into the structure of the Turing degrees. The following survey lists only some of the many known results. One general conclusion that can be drawn from the research is that the structure of the Turing degrees is extremely complicated.

### Order properties

- There are **minimal degrees**. A degree **a** is *minimal* if **a** is nonzero and there is no degree between **0** and **a**. Thus the order relation on the degrees is not a dense order.
- The Turing degrees are not linearly ordered by ≤T.
- In fact, for every nonzero degree **a** there is a degree **b** incomparable with **a**.
- There is a set of $2^{\aleph _{0}}$ pairwise incomparable Turing degrees.
- There are pairs of degrees with no greatest lower bound. Thus ${\mathcal {D}}$ is not a lattice.
- Every countable partially ordered set can be embedded in the Turing degrees.
- An infinite strictly increasing sequence **a**1, **a**2, ... of Turing degrees cannot have a least upper bound, but it always has an *exact pair* **c**, **d** such that ∀**e** (**e**<**c**∧**e**<**d** ⇔ ∃*i* **e**≤**a***i*) (and thus it has upper bounds).
- Assuming the axiom of constructibility, it can be shown there is a maximal chain of degrees of order type $\omega _{1}$ .

### Properties involving the jump

- For every degree **a** there is a degree strictly between **a** and **a**′. In fact, there is a countably infinite family of pairwise incomparable degrees between **a** and **a**′.
- Jump inversion: a degree **a** is of the form **b**′ if and only if **0**′ ≤ **a**.
- For any degree **a** there is a degree **b** such that **a** < **b** and **b**′ = **a**′; such a degree **b** is called *low* relative to **a**.
- There is an infinite sequence **a***i* of degrees such that **a**′*i*+1 ≤ **a***i* for each *i*.
- Post's theorem establishes a close correspondence between the arithmetical hierarchy and finitely iterated Turing jumps of the empty set.

### Logical properties

- Simpson (1977b) showed that the first-order theory of ${\mathcal {D}}$ in the language ⟨ ≤, = ⟩ or ⟨ ≤, ′, = ⟩ is many-one equivalent to the theory of true second-order arithmetic. This indicates that the structure of ${\mathcal {D}}$ is extremely complicated.
- Shore & Slaman (1999) showed that the jump operator is definable in the first-order structure of ${\mathcal {D}}$ with the language ⟨ ≤, = ⟩.

## Recursively enumerable Turing degrees

A degree is called *recursively enumerable* (r.e.) or *computably enumerable* (c.e.) if it contains a recursively enumerable set. Every r.e. degree is below **0**′, but not every degree below **0**′ is r.e.. However, a set A is many-one reducible to **0**′ if and only if A is r.e..

- Sacks (1964): The r.e. degrees are dense; between any two r.e. degrees there is a third r.e. degree.
- Lachlan (1966a) and Yates (1966): There are two r.e. degrees with no greatest lower bound in the r.e. degrees.
- Lachlan (1966a) and Yates (1966): There is a pair of nonzero r.e. degrees whose greatest lower bound is **0**.
- Lachlan (1966b): There is no pair of r.e. degrees whose greatest lower bound is **0** and whose least upper bound is **0**′. This result is informally called the *nondiamond theorem*.
- Thomason (1971): Every finite distributive lattice can be embedded into the r.e. degrees. In fact, the countable atomless Boolean algebra can be embedded in a manner that preserves suprema and infima.
- Lachlan & Soare (1980): Not all finite lattices can be embedded in the r.e. degrees (via an embedding that preserves suprema and infima). A particular example is shown to the right.
- L. A. Harrington and T. A. Slaman (see Nies, Shore & Slaman (1998)): The first-order theory of the r.e. degrees in the language ⟨ **0**, ≤, = ⟩ is many-one equivalent to the theory of true first-order arithmetic.

Additionally, there is Shoenfield's limit lemma, a set *A* satisfies $[A]\leq _{T}\emptyset '$ if and only if there is a "recursive approximation" to its characteristic function: a function *g* such that for sufficiently large *s*, $g(s)=\chi _{A}(s)$ .

A set *A* is called *n*-r e. if there is a family of functions $(A_{s})_{s\in \mathbb {N} }$ such that:

- *A**s* is a recursive approximation of *A*: for some *t*, for any *s*≥*t* we have *A**s*(*x*) = *A*(*x*), in particular conflating *A* with its characteristic function. *(Removing this condition yields a definition of* A *being* "weakly *n*-r.e."*)*
- *A**s* is an "*n*-trial predicate": for all *x*, *A*0(*x*)=0 and the cardinality of $\{s\mid A_{s}(x)\neq A_{s+1}(x)\}$ is ≤*n*.

Properties of *n*-r.e. degrees:

- The class of sets of *n*-r.e. degree is a strict subclass of the class of sets of (*n*+1)-r.e. degree.
- For all *n*>1 there are two (*n*+1)-r.e. degrees **a**, **b** with $\mathbf {a} \leq _{T}\mathbf {b}$ , such that the segment $\{\mathbf {c} \mid \mathbf {a} \leq _{T}\mathbf {c} \leq _{T}\mathbf {b} \}$ contains no *n*-r.e. degrees.
- A and ${\overline {A}}$ are (*n*+1)-r.e. if and only if both sets are weakly-*n*-r.e.

## Post's problem and the priority method

Emil Post studied the r.e. Turing degrees and asked whether there is any r.e. degree strictly between **0** and **0**′. The problem of constructing such a degree (or showing that none exist) became known as **Post's problem**. This problem was solved independently by Friedberg and Muchnik in the 1950s, who showed that these intermediate r.e. degrees do exist (Friedberg–Muchnik theorem). Their proofs each developed the same new method for constructing r.e. degrees, which came to be known as the **priority method**. The priority method is now the main technique for establishing results about r.e. sets.

The idea of the priority method for constructing an r.e. set *X* is to list a countable sequence of *requirements* that *X* must satisfy. For example, to construct an r.e. set *X* between **0** and **0**′ it is enough to satisfy the requirements *Ae* and *Be* for each natural number *e*, where *Ae* requires that the oracle machine with index *e* does not compute 0′ from *X* and *Be* requires that the Turing machine with index *e* (and no oracle) does not compute *X*. These requirements are put into a *priority ordering*, which is an explicit bijection of the requirements and the natural numbers. The proof proceeds inductively with one stage for each natural number; these stages can be thought of as steps of time during which the set *X* is enumerated. At each stage, numbers may be put into *X* or forever (if not injured) prevented from entering *X* in an attempt to *satisfy* requirements (that is, force them to hold once all of *X* has been enumerated). Sometimes, a number can be enumerated into *X* to satisfy one requirement but doing this would cause a previously satisfied requirement to become unsatisfied (that is, to be *injured*). The priority order on requirements is used to determine which requirement to satisfy in this case. The informal idea is that if a requirement is injured then it will eventually stop being injured after all higher priority requirements have stopped being injured, although not every priority argument has this property. An argument must be made that the overall set *X* is r.e. and satisfies all the requirements. Priority arguments can be used to prove many facts about r.e. sets; the requirements used and the manner in which they are satisfied must be carefully chosen to produce the required result.

For example, a simple (and hence noncomputable r.e.) low *X* (low means *X*′=0′) can be constructed in infinitely many stages as follows. At the start of stage *n*, let *T**n* be the output (binary) tape, identified with the set of cell indices where we placed 1 so far (so *X*=∪*n* *T**n*; *T*0=∅); and let *P**n*(*m*) be the priority for not outputting 1 at location *m*; *P*0(*m*)=∞. At stage *n*, if possible (otherwise do nothing in the stage), pick the least *i*<*n* such that ∀*m* *P**n*(*m*)≠*i* and Turing machine *i* halts in <*n* steps on some input *S*⊇*T**n* with ∀*m*∈*S*\*T**n* *P**n*(*m*)≥*i*. Choose any such (finite) *S*, set *T**n*+1=*S*, and for every cell *m* visited by machine *i* on *S*, set *P**n*+1(*m*) = min(*i*, *P**n*(*m*)), and set all priorities >*i* to ∞, and then set one priority ∞ cell (any will do) not in *S* to priority *i*. Essentially, we make machine *i* halt if we can do so without upsetting priorities <*i*, and then set priorities to prevent machines >*i* from disrupting the halt; all priorities are eventually constant.

To see that *X* is low, machine *i* halts on *X* if and only if it halts in <*n* steps on some *T**n* such that machines <*i* that halt on *X* do so <*n*−*i* steps (by recursion, this is uniformly computable from 0′). *X* is noncomputable since otherwise a Turing machine could halt on *Y* if and only if *Y*\*X* is nonempty, contradicting the construction since *X* excludes some priority *i* cells for arbitrarily large *i*; and *X* is simple because for each *i* the number of priority *i* cells is finite.
