---
title: "Potential game"
source: https://en.wikipedia.org/wiki/Potential_game
domain: algorithmic-game-theory
license: CC-BY-SA-4.0
tags: algorithmic game theory, computational equilibrium, combinatorial auction, selfish routing
fetched: 2026-07-02
---

# Potential game

In game theory, a game is said to be a **potential game** if the incentive of all players to change their strategy can be expressed using a single global function called the **potential function**. The concept originated in a 1996 paper by Dov Monderer and Lloyd Shapley.

The properties of several types of potential games have since been studied. Games can be either *ordinal* or *cardinal* potential games. In cardinal games, the difference in individual payoffs for each player from individually changing one's strategy, other things equal, has to have the same value as the difference in values for the potential function. In ordinal games, only the signs of the differences have to be the same.

The potential function is a useful tool to analyze equilibrium properties of games, since the incentives of all players are mapped into one function, and the set of pure Nash equilibria can be found by locating the local optima of the potential function. Convergence and finite-time convergence of an iterated game towards a Nash equilibrium can also be understood by studying the potential function.

Potential games can be studied as repeated games with state so that every round played has a direct consequence on game's state in the next round. This approach has applications in distributed control such as distributed resource allocation, where players without a central correlation mechanism can cooperate to achieve a globally optimal resource distribution.

## Definition

Let N be the number of players, A the set of action profiles over the action sets $A_{i}$ of each player and $u_{i}:A\to \mathbb {R}$ be the payoff function for player $1\leq i\leq N$ .

Given a game $G=(N,A=A_{1}\times \ldots \times A_{N},u:A\rightarrow \mathbb {R} ^{N})$ , we say that G is a **potential game** with an exact (weighted, ordinal, generalized ordinal, best response) **potential function** if $\Phi :A\rightarrow \mathbb {R}$ is an exact (weighted, ordinal, generalized ordinal, best response, respectively) potential function for G . We define these notions below.

- $\Phi$ is called an **exact potential function** if $\forall i,\forall {a_{-i}\in A_{-i}},\ \forall {a'_{i},\ a''_{i}\in A_{i}}$ ,

$\Phi (a'_{i},a_{-i})-\Phi (a''_{i},a_{-i})=u_{i}(a'_{i},a_{-i})-u_{i}(a''_{i},a_{-i})$

That is: when player

i

switches from action

$a'$

to action

$a''$

, the change in the potential

$\Phi$

equals the change in the utility of that player.

- $\Phi$ is called a **weighted potential function** if there is a vector $w\in \mathbb {R} _{++}^{N}$ such that $\forall i,\forall {a_{-i}\in A_{-i}},\ \forall {a'_{i},\ a''_{i}\in A_{i}}$ ,

$\Phi (a'_{i},a_{-i})-\Phi (a''_{i},a_{-i})=w_{i}(u_{i}(a'_{i},a_{-i})-u_{i}(a''_{i},a_{-i}))$

That is: when a player switches action, the change in

$\Phi$

equals the change in the player's utility, times a positive player-specific weight. Every exact PF is a weighted PF with

w

i

=1 for all

i

.

- $\Phi$ is called an **ordinal potential function** if $\forall i,\forall {a_{-i}\in A_{-i}},\ \forall {a'_{i},\ a''_{i}\in A_{i}}$ ,

$u_{i}(a'_{i},a_{-i})-u_{i}(a''_{i},a_{-i})>0\Leftrightarrow \Phi (a'_{i},a_{-i})-\Phi (a''_{i},a_{-i})>0$

That is: when a player switches action, the

sign

of the change in

$\Phi$

equals the

sign

of the change in the player's utility, whereas the magnitude of change may differ. Every weighted PF is an ordinal PF.

- $\Phi$ is called a **generalized ordinal potential function** if $\forall i,\forall {a_{-i}\in A_{-i}},\ \forall {a'_{i},\ a''_{i}\in A_{i}}$ ,

$u_{i}(a'_{i},a_{-i})-u_{i}(a''_{i},a_{-i})>0\Rightarrow \Phi (a'_{i},a_{-i})-\Phi (a''_{i},a_{-i})>0$

That is: when a player switches action, if the player's utility increases, then the potential increases (but the opposite is not necessarily true). Every ordinal PF is a generalized-ordinal PF.

- $\Phi$ is called a **best-response potential function** if $\forall i\in N,\ \forall {a_{-i}\in A_{-i}}$ ,

$\arg \max _{a_{i}\in A_{i}}u_{i}(a_{i},a_{-i})=\arg \max _{a_{i}\in A_{i}}\Phi (a_{i},a_{-i})$

. That is: for each player

i

, maximizing the common potential function leads to the same outcome as maximizing his own utility.

- $\Phi$ is called a **pseudo-potential function** if $\forall i\in N,\ \forall {a_{-i}\in A_{-i}}$ ,

$\arg \max _{a_{i}\in A_{i}}u_{i}(a_{i},a_{-i})\supseteq \arg \max _{a_{i}\in A_{i}}\Phi (a_{i},a_{-i})$

. That is: for each player

i

, maximizing the common potential function leads to

some

best response.

Note that while there are N utility functions, one for each player, there is only one potential function. Thus, through the lens of potential functions, the players become interchangeable (in the sense of one of the definitions above). Because of this *symmetry* of the game, decentralized algorithms based on the shared potential function often lead to convergence (in some of sense) to a Nash equilibria.

## A simple example

In *a* 2-player, 2-action game with externalities, individual players' payoffs are given by the function *u**i*(*a**i*, *a**j*) = *b**i* *a**i* + *w* *a**i* *a**j*, where *a**i* is players i's action, *a**j* is the opponent's action, and *w* is *a* positive externality from choosing the same action. The action choices are +1 and −1, as seen in the payoff matrix in Figure 1.

This game has *a* potential function P(*a*1, *a*2) = *b*1 *a*1 + *b*2 *a*2 + *w* *a*1 *a*2.

If player 1 moves from −1 to +1, the payoff difference is Δ*u*1 = *u*1(+1, *a*2) – *u*1(–1, *a*2) = 2 *b*1 + 2 *w* *a*2.

The change in potential is ΔP = P(+1, *a*2) – P(–1, *a*2) = (*b*1 + *b*2 *a*2 + *w* *a*2) – (–*b*1 + *b*2 *a*2 – *w* *a*2) = 2 *b*1 + 2 *w* *a*2 = Δ*u*1.

The solution for player 2 is equivalent. Using numerical values *b*1 = 2, *b*2 = −1, *w* = 3, this example transforms into *a* simple battle of the sexes, as shown in Figure 2. The game has two pure Nash equilibria, (+1, +1) and (−1, −1). These are also the local maxima of the potential function (Figure 3). The only stochastically stable equilibrium is (+1, +1), the global maximum of the potential function.

| +1 –1 +1 +*b*1+*w*, +*b*2+*w* +*b*1–*w*, –*b*2–*w* –1 –*b*1–*w*, +*b*2–*w* –*b*1+*w*, –*b*2+*w* *Fig. 1: Potential game example* | +1 –1 +1 5, 2 –1, –2 –1 –5, –4 1, 4 *Fig. 2: Battle of the sexes (payoffs)* | +1 –1 +1 **4** **0** –1 **–6** **2** *Fig. 3: Battle of the sexes (potentials)* |
|---|---|---|

A 2-player, 2-action game cannot be *a* potential game unless

$[u_{1}(+1,-1)+u_{1}(-1,+1)]-[u_{1}(+1,+1)+u_{1}(-1,-1)]=[u_{2}(+1,-1)+u_{2}(-1,+1)]-[u_{2}(+1,+1)+u_{2}(-1,-1)]$

## Potential games and congestion games

Exact potential games are equivalent to congestion games: Rosenthal proved that every congestion game has an exact potential; Monderer and Shapley proved the opposite direction: every game with an exact potential function is a congestion game.

The class of *ordinal* potential games is much larger. Fabrikant, Papadimitriou and Talwar proved that, for every problem in the complexity class PLS (essentially, every local search problem), there exists an ordinal potential game with polynomially many players, such that the set of pure Nash equilibria equals the set of local optima.

## Potential games and improvement paths

An **improvement path** (also called **Nash dynamics**) is a sequence of strategy-vectors, in which each vector is attained from the previous vector by a single player switching his strategy to a strategy that strictly increases his utility. If a game has a generalized-ordinal-potential function $\Phi$ , then $\Phi$ is strictly increasing in every improvement path, so every improvement path is acyclic. If, in addition, the game has finitely many strategies, then every improvement path must be finite. This property is called the **finite improvement property (FIP)**. We have just proved that every finite generalized-ordinal-potential game has the FIP. The opposite is also true: every finite game has the FIP has a generalized-ordinal-potential function. The terminal state in every finite improvement path is a Nash equilibrium, so FIP implies the existence of a pure-strategy Nash equilibrium. Moreover, it implies that a Nash equilibrium can be computed by a distributed process, in which each agent only has to improve his own strategy.

A **best-response path** is a special case of an improvement path, in which each vector is attained from the previous vector by a single player switching his strategy to a best-response strategy. The property that every best-response path is finite is called the **finite best-response property (FBRP)**. FBRP is weaker than FIP, and it still implies the existence of a pure-strategy Nash equilibrium. It also implies that a Nash equilibrium can be computed by a distributed process, but the computational burden on the agents is higher than with FIP, since they have to compute a best-response.

An even weaker property is **weak-acyclicity (WA)**. It means that, for any initial strategy-vector, *there exists* a finite best-response path starting at that vector. Weak-acyclicity is not sufficient for existence of a potential function (since some improvement-paths may be cyclic), but it is sufficient for the existence of pure-strategy Nash equilibrium. It implies that a Nash equilibrium can be computed almost-surely by a stochastic distributed process, in which at each point, a player is chosen at random, and this player chooses a best-strategy at random.

## Pseudo-potential games

Dubey, Haimanko and Zapechelnyuk prove:

- Any game of weak strategic substitutes or strategic complements with aggregation is a pseudo-potential game.
- Any pseudo-potential game has a pure-strategy Nash equilibrium.

## Correlated equilibria

Abraham Neyman studied potential games in which (a) the potential is a smooth and concave function, (b) the strategy sets are convex, (c) the utilities are bounded. He proves that, in such games, any correlated equilibrium is a mixture of pure strategy profiles which maximize the potential.

If, in addition, (d) the strategy sets are compact, (e) the potential is a strictly concave function, then the correlated equilibrium is unique.
