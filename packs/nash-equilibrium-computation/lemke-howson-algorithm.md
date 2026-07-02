---
title: "Lemke–Howson algorithm"
source: https://en.wikipedia.org/wiki/Lemke%E2%80%93Howson_algorithm
domain: nash-equilibrium-computation
license: CC-BY-SA-4.0
tags: nash equilibrium computation, lemke howson algorithm, ppad complete, fixed point argument
fetched: 2026-07-02
---

# Lemke–Howson algorithm

The **Lemke–Howson algorithm** is an algorithm that computes a Nash equilibrium of a bimatrix game, named after its inventors, Carlton E. Lemke and J. T. Howson. It is said to be "the best known among the combinatorial algorithms for finding a Nash equilibrium", although more recently the Porter-Nudelman-Shoham algorithm has outperformed on a number of benchmarks.

## Description

The input to the algorithm is a 2-player game *G*. Here, *G* is represented by two *m* × *n* game matrices *A* and *B*, containing the payoffs for players 1 and 2 respectively, who have *m* and *n* pure strategies respectively. In the following, one assumes that all payoffs are positive. (By rescaling, any game can be transformed into a strategically equivalent game with positive payoffs.)

*G* has two corresponding polytopes (called the *best-response polytopes*) *P*1 and *P*2, in *m* dimensions and *n* dimensions respectively, defined as follows:

- *P*1 is in **R***m*; let {*x*1,...,*x**m*} denote the coordinates. *P*1 is defined by *m* inequalities *x**i* ≥ 0, for all *i* ∈ {1,...,*m*}, and a further *n* inequalities $B_{1,j}x_{1}+\dots +B_{m,j}x_{m}\leq 1,$ for all *j* ∈ {1,...,*n*}.
- *P*2 is in **R***n*; let {*x**m*+1,...,*x**m*+*n*} denote the coordinates. *P*2 is defined by *n* inequalities *x**m*+*i* ≥ 0, for all *i* ∈ {1,...,*n*}, and a further *m* inequalities $A_{i,1}x_{m+1}+\dots +A_{i,n}x_{m+n}\leq 1,$ for all *i* ∈ {1,...,*m*}.

Here, *P*1 represents the set of unnormalized probability distributions over player 1's *m* pure strategies, such that player 2's expected payoff is at most 1. The first *m* constraints require the probabilities to be non-negative, and the other *n* constraints require each of the *n* pure strategies of player 2 to have an expected payoff of at most 1. *P*2 has a similar meaning, reversing the roles of the players.

Each vertex *v* of *P*1 is associated with a set of labels from the set {1,...,*m* + *n*} as follows. For *i* ∈ {1, ..., *m*}, vertex *v* gets the label *i* if *x**i* = 0 at vertex *v*. For *j* ∈ {1, ..., *n*}, vertex *v* gets the label *m* + *j* if $B_{1,j}x_{1}+\dots +B_{m,j}x_{m}=1.$ Assuming that *P*1 is nondegenerate, each vertex is incident to *m* facets of *P*1 and has *m* labels. Note that the origin, which is a vertex of *P*1, has the labels {1, ..., *m*}.

Each vertex *w* of *P*2 is associated with a set of labels from the set {1, ..., *m* + *n*} as follows. For *j* ∈ {1, ..., *n*}, vertex *w* gets the label *m* + *j* if *x**m*+*j* = 0 at vertex *w*. For *i* ∈ {1, ..., *m*}, vertex *w* gets the label *i* if $A_{i,1}x_{m+1}+\dots +A_{i,n}x_{m+n}=1.$ Assuming that *P*2 is nondegenerate, each vertex is incident to *n* facets of *P*2 and has *n* labels. Note that the origin, which is a vertex of *P*2, has the labels {*m* + 1, ..., *m* + *n*}.

Consider pairs of vertices (*v*,*w*), *v* ∈ *P*1, *w* ∈ *P*2. The pairs of vertices (*v*,*w*) is said to be *completely labeled* if the sets associated with *v* and *w* contain all labels {1, ..., *m* + *n*}. Note that if *v* and *w* are the origins of **R***m* and **R***n* respectively, then (*v*,*w*) is completely labeled. The pairs of vertices (*v*,*w*) is said to be *almost completely labeled* (with respect to some missing label *g*) if the sets associated with *v* and *w* contain all labels in {1, ..., *m* + *n*} other than *g*. Note that in this case, there will be a *duplicate label* that is associated with both *v* and *w*.

A *pivot operation* consists of taking some pair (*v*,*w*) and replacing *v* with some vertex adjacent to *v* in *P*1, or alternatively replacing *w* with some vertex adjacent to *w* in *P*2. This has the effect (in the case that *v* is replaced) of replacing some label of *v* with some other label. The replaced label is said to be *dropped*. Given any label of *v*, it is possible to drop that label by moving to a vertex adjacent to *v* that does not contain the hyperplane associated with that label.

The algorithm starts at the completely labeled pair (*v*,*w*) consisting of the pair of origins. An arbitrary label *g* is dropped via a pivot operation, taking us to an almost completely labeled pair (*v′*,*w′*). Any almost completely labeled pair admits two pivot operations corresponding to dropping one or other copy of its duplicated label, and each of these operations may result in another almost completely labeled pair, or a completely labeled pair. Eventually, the algorithm finds a completely labeled pair (*v**,*w**), which is not the origin. (*v**,*w**) corresponds to a pair of unnormalised probability distributions in which every strategy *i* of player 1 either pays that player 1, or pays less than 1 and is played with probability 0 by that player (and a similar observation holds for player 2). Normalizing these values to probability distributions, one has a Nash equilibrium (whose payoffs to the players are the inverses of the normalization factors).

## Properties

The algorithm can find at most *n* + *m* different Nash equilibria. Any choice of initially dropped label determines the equilibrium that is eventually found by the algorithm.

The Lemke–Howson algorithm is equivalent to the following homotopy-based approach. Modify *G* by selecting an arbitrary pure strategy *g*, and giving the player who owns that strategy, a large payment *B* to play it. In the modified game, the strategy *g* is played with probability 1, and the other player will play their best response to *g* with probability 1. Consider the continuum of games in which *B* is continuously reduced to 0. There exists a path of Nash equilibria connecting the unique equilibrium of the modified game, to an equilibrium of *G*. The pure strategy *g* chosen to receive the bonus *B* corresponds to the initially dropped label. While the algorithm is efficient in practice, in the worst case the number of pivot operations may need to be exponential in the number of pure strategies in the game. Subsequently, it has been shown that it is PSPACE-complete to find any of the solutions that can be obtained with the Lemke–Howson algorithm.
