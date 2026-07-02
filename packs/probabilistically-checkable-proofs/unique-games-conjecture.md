---
title: "Unique games conjecture"
source: https://en.wikipedia.org/wiki/Unique_games_conjecture
domain: probabilistically-checkable-proofs
license: CC-BY-SA-4.0
tags: probabilistically checkable proof, pcp theorem, proof verification, hardness of approximation
fetched: 2026-07-02
---

# Unique games conjecture

Unsolved problem in computer science

Is the Unique Games Conjecture true?

More unsolved problems in computer science

In computational complexity theory, the **unique games conjecture** (often referred to as **UGC**) is a conjecture made by Subhash Khot in 2002. The conjecture postulates that the problem of determining the approximate *value* of a certain type of game, known as a *unique game*, has NP-hard computational complexity. It has broad applications in the theory of hardness of approximation. If the unique games conjecture is true and P ≠ NP, then for many important problems it is not only impossible to get an exact solution in polynomial time (as postulated by the P versus NP problem), but also impossible to get a good polynomial-time approximation. The problems for which such an inapproximability result would hold include constraint satisfaction problems, which crop up in a wide variety of disciplines.

According to Ryan O'Donnell as quoted by the Simons Foundation, academics are roughly evenly divided on whether the conjecture is true or false.

## Formulations

The unique games conjecture can be stated in a number of equivalent ways.

### Unique label cover

The following formulation of the unique games conjecture is often used in hardness of approximation. The conjecture postulates the NP-hardness of the following promise problem known as *label cover with unique constraints*. For each edge, the colors on the two vertices are restricted to some particular ordered pairs. *Unique* constraints means that for each edge none of the ordered pairs have the same color for the same node.

This means that an instance of label cover with unique constraints over an alphabet of size k can be represented as a directed graph together with a collection of permutations $\pi _{e}:[k]\to [k]$ , one for each edge e of the graph. An assignment to a label cover instance gives to each vertex of G a value in the set $[k]=\{1,2,\ldots ,k\}$ , often called “colours”.

- (An instance of unique label cover. The 4 vertices may be assigned the colors red, blue, and green while satisfying the constraints at each edge.) An instance of unique label cover. The 4 vertices may be assigned the colors red, blue, and green while satisfying the constraints at each edge.
- (A solution to the unique label cover instance.) A solution to the unique label cover instance.

Such instances are strongly constrained in the sense that the colour of a vertex uniquely defines the colours of its neighbours, and hence for its entire connected component. Thus, if the input instance admits a valid assignment, then such an assignment can be found efficiently by iterating over all colours of a single node. In particular, the problem of deciding if a given instance admits a satisfying assignment can be solved in polynomial time.

- (An instance of unique label cover that does not allow a satisfying assignment.) An instance of unique label cover that does not allow a satisfying assignment.
- (An assignment that satisfies all edges except the thick edge. Thus, this instance has value 3/4.) An assignment that satisfies all edges except the thick edge. Thus, this instance has value 3/4.

The *value* of a unique label cover instance is the fraction of constraints that can be satisfied by any assignment. For satisfiable instances, this value is 1 and is easy to find. On the other hand, it seems to be very difficult to determine the value of an unsatisfiable game, even approximately. The unique games conjecture formalises this difficulty.

More formally, the $(c,s)$ -gap label-cover problem with unique constraints is the following promise problem $(L_{\text{yes}},L_{\text{no}})$ :

- $L_{\text{yes}}=\{G:{\text{some assignment satisfies at least a }}c{\text{-fraction of constraints in }}G\}$ ,
- $L_{\text{no}}=\{G:{\text{every assignment satisfies at most an }}s{\text{-fraction of constraints in }}G\}$ ,

where G is an instance of the label cover problem with unique constraints.

The unique games conjecture states that for every sufficiently small pair of constants $\varepsilon ,\delta >0$ , there exists a constant k such that the $(1-\delta ,\varepsilon )$ -gap label-cover problem with unique constraints over alphabet of size k is NP-hard.

### Maximizing linear equations modulo *k*

Consider the following system of linear equations over the integers modulo k : ${\begin{aligned}a_{1}x_{1}&\equiv b_{1}\cdot x_{2}+c_{1}{\pmod {k}},\\a_{2}x_{2}&\equiv b_{2}\cdot x_{5}+c_{2}{\pmod {k}},\\&{}\ \ \vdots \\a_{m}x_{1}&\equiv b_{m}\cdot x_{7}+c_{m}{\pmod {k}}.\end{aligned}}$ When each equation involves exactly two variables, this is an instance of the label cover problem with unique constraints; such instances are known as instances of the Max2Lin(k) problem. It is not immediately obvious that the inapproximability of Max2Lin(k) is equivalent to the UGC, but this is in fact the case, by a reduction. Namely, the UGC is equivalent to: for every sufficiently small pair of constants *ε*, *δ* > 0, there exists a constant *k* such that the (1 − *δ*, *ε*)-gap Max2Lin(k) problem is NP-hard.

### Connection with computational topology

It has been argued that the UGC is essentially a question of computational topology, involving local-global principles (the latter are also evident in the proof of the 2-2 Games Conjecture, see below).

Linial observed that unique label cover is an instance of the Maximum Section of a Covering Graph problem (covering graphs is the terminology from topology; in the context of unique games these are often referred to as graph lifts). To date, all known problems whose inapproximability is equivalent to the UGC are instances of this problem, including Unique Label Cover and Max2Lin(k). When the latter two problems are viewed as instances of Max Section of a Covering Graph, the reduction between them preserves the structure of the graph covering spaces, so not only the problems, but the reduction between them has a natural topological interpretation. Grochow and Tucker-Foltz exhibited a third computational topology problem whose inapproximability is equivalent to the UGC: 1-Cohomology Localization on Triangulations of 2-Manifolds.

### Two-prover proof systems

A **unique game** is a special case of a *two-prover one-round (2P1R) game*. A two-prover one-round game has two players (also known as provers) and a referee. The referee sends each player a question drawn from a known probability distribution, and the players each have to send an answer. The answers come from a set of fixed size. The game is specified by a predicate that depends on the questions sent to the players and the answers provided by them.

The players may decide on a strategy beforehand, although they cannot communicate with each other during the game. The players win if the predicate is satisfied by their questions and their answers.

A two-prover one-round game is called a *unique game* if for every question and every answer by the first player, there is exactly one answer by the second player that results in a win for the players, and vice versa. The *value* of a game is the maximum winning probability for the players over all strategies.

The **unique games conjecture** states that for every sufficiently small pair of constants *ε*, *δ* > 0, there exists a constant *k* such that the following promise problem (*L*yes, *L*no) is NP-hard:

- *L*yes = {*G*: the value of *G* is at least 1 − δ}
- *L*no = {*G*: the value of *G* is at most ε}

where *G* is a unique game whose answers come from a set of size *k*.

### Probabilistically checkable proofs

Alternatively, the unique games conjecture postulates the existence of a certain type of probabilistically checkable proof for problems in NP.

A unique game can be viewed as a special kind of nonadaptive probabilistically checkable proof with query complexity 2, where for each pair of possible queries of the verifier and each possible answer to the first query, there is exactly one possible answer to the second query that makes the verifier accept, and vice versa.

The unique games conjecture states that for every sufficiently small pair of constants $\varepsilon ,\delta >0$ there is a constant K such that every problem in NP has a probabilistically checkable proof over an alphabet of size K with completeness $1-\delta$ , soundness $\varepsilon$ , and randomness complexity $O(\log n)$ which is a unique game.

## Relevance

| Problem | Poly.-time approx. | NP hardness | UG hardness |
|---|---|---|---|
| Max 2SAT | $0.940\dots$ | $0.954\dots +\varepsilon$ | $0.940\dots +\varepsilon$ |
| Max cut | $0.878...\dots$ | ${\tfrac {16}{17}}+\varepsilon \approx 0.941$ | $0.878\dots +\varepsilon$ |
| Min vertex cover | 2 | ${\sqrt {2}}-\varepsilon$ | $2-\varepsilon$ |
| Feedback arc set | $O(\log n\log \log n)$ | $1.360\dots -\varepsilon$ | All constants |
| Max acyclic subgraph | ${\tfrac {1}{2}}+\Omega (1/{\sqrt {\Delta }})$ | ${\tfrac {2}{3}}+\varepsilon$ | ${\tfrac {1}{2}}+\varepsilon$ |
| Betweenness | ${\tfrac {1}{3}}$ | ${\tfrac {1}{2}}+\varepsilon$ | ${\tfrac {1}{3}}+\varepsilon$ |

> Some very natural, intrinsically interesting statements about things like voting and foams just popped out of studying the UGC.... Even if the UGC turns out to be false, it has inspired a lot of interesting math research.

— Ryan O’Donnell,

The unique games conjecture was introduced by Subhash Khot in 2002 in order to make progress on certain questions in the theory of hardness of approximation.

The truth of the unique games conjecture would imply the optimality of many known approximation algorithms (assuming P ≠ NP). For example, the approximation ratio achieved by the algorithm of Goemans and Williamson for approximating the maximum cut in a graph is optimal to within any additive constant assuming the unique games conjecture and P ≠ NP.

A list of results that the unique games conjecture is known to imply is shown in the adjacent table together with the corresponding best results for the weaker assumption P ≠ NP. A constant of $c+\varepsilon$ or $c-\varepsilon$ means that the result holds for every *constant* (with respect to the problem size) strictly greater than or less than c , respectively.

## Discussion and alternatives

Currently, there is no consensus regarding the truth of the unique games conjecture. Certain stronger forms of the conjecture have been disproved.

A different form of the conjecture postulates that distinguishing the case when the value of a unique game is at least $1-\delta$ from the case when the value is at most $\varepsilon$ is impossible for polynomial-time algorithms (but perhaps not NP-hard). This form of the conjecture would still be useful for applications in hardness of approximation.

The constant $\delta >0$ in the above formulations of the conjecture is necessary unless P = NP. If the uniqueness requirement is removed the corresponding statement is known to be true by the parallel repetition theorem, even when $\delta =0$ .

## Results

Marek Karpinski and Warren Schudy have constructed linear time approximation schemes for dense instances of unique games problem.

In 2008, Prasad Raghavendra has shown that if the unique games conjecture is true, then for every constraint satisfaction problem the best approximation ratio is given by a certain simple semidefinite programming instance, which is in particular polynomial.

In 2010, Prasad Raghavendra and David Steurer defined the *gap-small-set expansion* problem, and conjectured that it is NP-hard. The resulting small set expansion hypothesis implies the unique games conjecture. It has also been used to prove strong hardness of approximation results for finding complete bipartite subgraphs.

In 2010, Sanjeev Arora, Boaz Barak and David Steurer found a subexponential time approximation algorithm for the unique games problem. A key ingredient in their result was the spectral algorithm of Alexandra Kolla (see also the earlier manuscript of A. Kolla and Madhur Tulsiani). The latter also re-proved that unique games on expander graphs could be solved in polynomial time, and was one of (if not the) first graph algorithms to take advantage of the full spectrum of a graph rather than just its first two eigenvalues.

In 2012, it was shown that distinguishing instances with value at most ${\tfrac {3}{8}}+\delta$ from instances with value at least ${\tfrac {1}{2}}$ is NP-hard.

In 2018, after a series of papers, a weaker version of the conjecture, called the 2-2 games conjecture, was proven. In a certain sense, this proves "a half" of the original conjecture. This also improves the best known gap for unique label cover: it is NP-hard to distinguish instances with value at most $\delta$ from instances with value at least ${\tfrac {1}{2}}$ .
