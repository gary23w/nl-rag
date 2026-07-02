---
title: "Price of stability"
source: https://en.wikipedia.org/wiki/Price_of_stability
domain: price-of-anarchy
license: CC-BY-SA-4.0
tags: price of anarchy, price of stability, congestion game, braess paradox
fetched: 2026-07-02
---

# Price of stability

In game theory, the **price of stability (PoS)** of a game is the ratio between the best objective function value of one of its equilibria and that of an optimal outcome. The PoS is relevant for games in which there is some objective authority that can influence the players a bit, and maybe help them converge to a good Nash equilibrium. When measuring how efficient a Nash equilibrium is in a specific game we often also talk about the price of anarchy (PoA), which is the ratio between the *worst* objective function value of one of its equilibria and that of an optimal outcome.

## Examples

Another way of expressing PoS is:

${\text{PoS}}={\frac {\text{value of best Nash equilibrium}}{\text{value of optimal solution}}},\ {\text{PoS}}\geq 0.$

In particular, if the optimal solution is a Nash equilibrium, then the PoS is 1.

In the following prisoner’s dilemma game, since there is a single equilibrium $(B,R)$ we have PoS = PoA = 1/2.

|   | Left | Right |
|---|---|---|
| Top | (2,2) | (0,3) |
| Bottom | (3,0) | (1,1) |

On this example which is a version of the battle of sexes game, there are two equilibrium points, $(T,L)$ and $(B,R)$ , with values 3 and 15, respectively. The optimal value is 15. Thus, PoS = 1 while PoA = 1/5.

|   | Left | Right |
|---|---|---|
| Top | (2,1) | (0,0) |
| Bottom | (0,0) | (5,10) |

## Background and milestones

The price of stability was first studied by A. Schulz and N. Stier-Moses, while the term was coined by E. Anshelevich et al. Schulz and Stier-Moses focused on equilibria in a selfish routing game in which edges have capacities. Anshelevich et al. studied network design games and showed that a pure strategy Nash equilibrium always exists with the price of stability in this game being at most the nth harmonic number in directed graphs. For undirected graphs, Anshelevich et al. presented a tight bound on the price of stability of 4/3 for a single source and two players case. Jian Li has proved that for undirected graphs with a distinguished destination to which all players must connect the price of stability of the Shapely network design game is $O(\log n/\log \log n)$ where n is the number of players. On the other hand, the price of anarchy is about n in this game.

## Network design games

### Setup

Network design games have a very natural motivation for the Price of Stability. In these games, the Price of Anarchy can be much worse than the Price of Stability.

Consider the following game.

- n players;
- Each player i aims to connect $s_{i}$ to $t_{i}$ on a directed graph $G=(V,E)$ ;
- The strategies $P_{i}$ for a player are all paths from $s_{i}$ to $t_{i}$ in G ;
- Each edge has a cost $c_{i}$ ;
- 'Fair cost allocation': When $n_{e}$ players choose edge e , the cost $\textstyle d_{e}(n_{e})={\frac {c_{e}}{n_{e}}}$ is split equally among them;
- The player cost is $\textstyle C_{i}(S)=\sum _{e\in P_{i}}{\frac {c_{e}}{n_{e}}}$
- The social cost is the sum of the player costs: $\textstyle SC(S)=\sum _{i}C_{i}(S)=\sum _{e\in S}n_{e}{\frac {c_{e}}{n_{e}}}=\sum _{e\in S}c_{e}$ .

### Price of anarchy

The price of anarchy can be $\Omega (n)$ . Consider the following network design game.

Consider two different equilibria in this game. If everyone shares the $1+\varepsilon$ edge, the social cost is $1+\varepsilon$ . This equilibrium is indeed optimal. Note, however, that everyone sharing the n edge is a Nash equilibrium as well. Each agent has cost 1 at equilibrium, and switching to the other edge raises his cost to $1+\varepsilon$ .

### Lower bound on price of stability

Here is a pathological game in the same spirit for the Price of Stability, instead. Consider n players, each originating from $s_{i}$ and trying to connect to t . The cost of unlabeled edges is taken to be 0.

The optimal strategy is for everyone to share the $1+\varepsilon$ edge, yielding total social cost $1+\varepsilon$ . However, there is a unique Nash for this game. Note that when at the optimum, each player is paying $\textstyle {\frac {1+\varepsilon }{n}}$ , and player 1 can decrease his cost by switching to the $\textstyle {\frac {1}{n}}$ edge. Once this has happened, it will be in player 2's interest to switch to the $\textstyle {\frac {1}{n-1}}$ edge, and so on. Eventually, the agents will reach the Nash equilibrium of paying for their own edge. This allocation has social cost $\textstyle 1+{\frac {1}{2}}+\cdots +{\frac {1}{n}}=H_{n}$ , where $H_{n}$ is the n th harmonic number, which is $\Theta (\log n)$ . Even though it is unbounded, the price of stability is exponentially better than the price of anarchy in this game.

### Upper bound on price of stability

Note that by design, network design games are congestion games. Therefore, they admit a potential function $\textstyle \Phi =\sum _{e}\sum _{i=1}^{n_{e}}{\frac {c_{e}}{i}}$ .

**Theorem.** [Theorem 19.13 from Reference 1] Suppose there exist constants A and B such that for every strategy S ,

$A\cdot SC(S)\leq \Phi (S)\leq B\cdot SC(S).$

Then the price of stability is less than $B/A$

*Proof.* The global minimum $NE$ of $\Phi$ is a Nash equilibrium, so

$SC(NE)\leq 1/A\cdot \Phi (NE)\leq 1/A\cdot \Phi (OPT)\leq B/A\cdot SC(OPT).$

Now recall that the social cost was defined as the sum of costs over edges, so

$\Phi (S)=\sum _{e\in S}\sum _{i=1}^{n_{e}}{\frac {c_{e}}{i}}=\sum _{e\in S}c_{e}H_{n_{e}}\leq \sum _{e\in S}c_{e}H_{n}=H_{n}\cdot SC(S).$

We trivially have $A=1$ , and the computation above gives $B=H_{n}$ , so we may invoke the theorem for an upper bound on the price of stability.
