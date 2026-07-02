---
title: "Correlated equilibrium"
source: https://en.wikipedia.org/wiki/Correlated_equilibrium
domain: nash-equilibrium-computation
license: CC-BY-SA-4.0
tags: nash equilibrium computation, lemke howson algorithm, ppad complete, fixed point argument
fetched: 2026-07-02
---

# Correlated equilibrium

In game theory, a **correlated equilibrium** is a solution concept that is more general than the well known Nash equilibrium. It was first discussed by mathematician Robert Aumann in 1974. The idea is that each player chooses their action according to their private observation of the value of the same public signal. A strategy assigns an action to every possible observation a player can make. If no player would want to deviate from their strategy (assuming the others also don't deviate), the distribution from which the signals are drawn is called a correlated equilibrium.

## Formal definition

An N -player strategic game $\displaystyle (N,\{A_{i}\},\{u_{i}\})$ is characterized by an action set $A_{i}$ and utility function $u_{i}$ for each player i . When player i chooses strategy $a_{i}\in A_{i}$ and the remaining players choose a strategy profile described by the $(N-1)$ -tuple $a_{-i}$ , then player i 's utility is $\displaystyle u_{i}(a_{i},a_{-i})$ .

A *strategy modification* for player i is a function $\phi _{i}\colon A_{i}\to A_{i}$ . That is, $\phi _{i}$ tells player i to modify his behavior by playing action $\phi _{i}(a_{i})$ when instructed to play $a_{i}$ .

Let $(\Omega ,\pi )$ be a countable probability space. For each player i , let $P_{i}$ be his information partition, $q_{i}$ be i 's posterior probability and let $s_{i}\colon \Omega \rightarrow A_{i}$ , assigning the same value to states in the same cell of i 's information partition. Then $((\Omega ,\pi ),P_{i},s_{i})$ is a correlated equilibrium of the strategic game $(N,A_{i},u_{i})$ if for every player i and for every strategy modification $\phi _{i}$ :

$\sum _{\omega \in \Omega }q_{i}(\omega )u_{i}(s_{i}(\omega ),s_{-i}(\omega ))\geq \sum _{\omega \in \Omega }q_{i}(\omega )u_{i}(\phi _{i}(s_{i}(\omega )),s_{-i}(\omega ))$

In other words, $((\Omega ,\pi ),P_{i})$ is a correlated equilibrium if no player can improve his or her expected utility via a strategy modification.

## An example

|   | **D**are | **C**hicken out |
|---|---|---|
| **D**are | 0, 0 | 7, 2 |
| **C**hicken out | 2, 7 | 6, 6 |
| *A game of Chicken* |   |   |

Consider the game of chicken pictured. In this game two individuals are challenging each other to a contest where each can either *dare* or *chicken out*. If one is going to dare, it is better for the other to chicken out. But if one is going to chicken out, it is better for the other to dare. This leads to an interesting situation where each wants to dare, but only if the other might chicken out.

In this game, there are three Nash equilibria. The two pure strategy Nash equilibria are (*D*, *C*) and (*C*, *D*). There is also a mixed strategy equilibrium where both players chicken out with probability 2/3.

Now consider a third party (or some natural event) that draws one of three cards labeled: (*C*, *C*), (*D*, *C*), and (*C*, *D*), with the same probability, i.e. probability 1/3 for each card. After drawing the card the third party informs the players of the strategies assigned to them and to their opponent on the card. Suppose a player is assigned *D*, they would not want to deviate supposing the other player played their assigned strategy since they will get 7 (the highest payoff possible). Suppose a player is assigned *C*. Then the other player will play *C* with probability 1/2 and *D* with probability 1/2. The expected utility of Daring is 7(1/2) + 0(1/2) = 3.5 and the expected utility of chickening out is 2(1/2) + 6(1/2) = 4. So, the player would prefer chickening out.

Since neither player has an incentive to deviate, this is a correlated equilibrium. The expected payoff for this equilibrium is 7(1/3) + 2(1/3) + 6(1/3) = 5 which is higher than the expected payoff of the mixed strategy Nash equilibrium.

The following correlated equilibrium has an even higher payoff to both players: Recommend (*C*, *C*) with probability 1/2, and (*D*, *C*) and (*C*, *D*) with probability 1/4 each. Then when a player is recommended to play *C*, they know that the other player will play *D* with (conditional) probability 1/3 and *C* with probability 2/3, and gets expected payoff 14/3, which is equal to (not less than) the expected payoff when they play *D*. In this correlated equilibrium, both players get 5.25 in expectation. It can be shown that this is the correlated equilibrium with maximal sum of expected payoffs to the two players.

## Learning correlated equilibria

One of the advantages of correlated equilibria is that they are computationally less expensive than Nash equilibria. This can be captured by the fact that computing a correlated equilibrium only requires solving a linear program whereas solving a Nash equilibrium requires finding its fixed point completely. Another way of seeing this is that it is possible for two players to respond to each other's historical plays of a game and end up converging to a correlated equilibrium.
